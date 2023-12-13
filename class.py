
class Patient():
    def __init__(self,id = 0,age=0,sexe=0,patho=0,arrivée=0) -> None:
        self.id = id
        self.age = age
        self.sexe = sexe 
        self.arrivéeUrgences = arrivée
        self.debutSoins = 0
        self.patho = patho 
        self.gravite = int(self.patho/2 + 1) #Arbitraire
        self.duree = int(self.patho/3 + 1) #Arbitraire
        self.state = 0 #0 Si en attente, 1 sinon
    
class Soignant():
    def __init__(self,id,competence) -> None:
        self.id = id
        self.competences = competence 
        self.state = 0

class Planning():
    def __init__(self,liste_soignant,liste_patient,Horizon) -> None:
        self.nSoignants = len(liste_soignant)
        self.nPatient = len(liste_patient)
        self.horizon = Horizon

        self.planning = self.generate_planning(liste_soignant,liste_patient)
    
      
    def generate_planning(liste_soignant,liste_patient): 
        '''
        Genère un planning incluant tout les rdvs. Le planning est une matrice Soignant x RDV
        Les rdvs sont ajoutés à la suite. Chaque rdv est caractérisé par l'id du patient et le temps de l'intervention.
        Ces plannings sont stables 
        '''
        n = len(liste_soignant)
        m = len(liste_patient)
        plan = []                
        pabon = []
        while (liste_patient!=[]): #Premier ajout des patients Certains peuvent ne pas être placés. Ajout rapide mais partiel
            L = []
            to_delete = []
            k = 0
            for soignant in liste_soignant :
                if k <= len(L) : #Dernière boucle 
                    patient = liste_patient[k]
                else : patient = Patient()
                k+=1
                if patient.patho in soignant.competences : 
                    L.append(patient)                    
                else : 
                    L.append(Patient())
                    pabon.append(patient)
            to_delete.append(patient)    
            plan.append(L)
            for patient in to_delete : liste_patient.remove(patient)

        while pabon != [] : #Deuxieme ajout, plus lent mais certains
            L = [Patient() for i in range(n)]
            to_delete = []
            for patient in pabon :                 
                for soignant_num in range(n) : 
                    if (patient.patho in soignant[soignant_num].competences) and (L[soignant_num]==Patient()) : 
                        L[soignant_num] = patient
                        to_delete.append(patient)
            plan.append(L)
            for patient in to_delete : pabon.remove(patient)            
        return plan 
    
    