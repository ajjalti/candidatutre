import os
import json
user=os.getlogin()
try:
    os.mkdir('/Users/'+user+'/Desktop/bachelier')
except OSError:
    pass
os.chdir('/Users/mac/Desktop/bachelier')
class Bachellier:
    def __init__(self):
        self.Num_ins=int(input('entrer nombre d\'nscription\n'))
        self.NP=input('entrer nom et prenom\n')
        self.FILIERE=input('entrer la fillière\n')
        self.MG=float(input('entrer la moyenne generale\n'))
        self.FS=float(input('formule spécifique\n'))
        self.i=float(input('doublant ou pas'))
    def saisir(self):
        with open('PSI.json','r+') as f:
            data = json.load(f)
        with open('PSI.json','w+') as f:
            data.append(self.__dict__)
            json.dump(data,f)
## formule generale:
def formule_Gen():
    with open('PSI.json','r+') as f:
        data=json.load(f)
        dat=[]
        for liste in data:
            FG=((liste["MG"]*5)+liste["FS"])+liste["i"]
            for i in range(3):liste.popitem()
            liste["FG"]=FG
            dat.append(liste)
    with open('PSI_FG.json','w+') as f:
        json.dump(dat,f)

## fonction pour classer les bachellier selon leurs formule globale:
def classer():
    with open('PSI_FG.json','r+') as f:
        data=json.load(f)
        new=sorted(data,key=lambda k:k['FG'],reverse=True)
    with open('PSI_FG.json','w+') as f:
        json.dump(new,f)

## fonction generer qui classe les bachellier 
# selon leurs orientation dans les quatres groupes disponible dans l'établissement selon leur note et formule global
def generer():
    with open('PSI_FG.json','r+') as f:
        data=json.load(f)
    svt=[i for i in data if i['FILIERE']=="svt"]
    sma=[i for i in data if i['FILIERE']=="sma"]
    smb=[i for i in data if i['FILIERE']=="smb"]
    pc=[i for i in data if i['FILIERE']=="pc"]
    with open('PSI_princ.json','r+') as f:
        data=json.load(f)
        for i in sma[:13]:
            data.append(i)
        for i in smb[:10]:
            data.append(i)
        for i in pc[:7]:
            data.append(i)
        for i in svt[:4]:
            data.append(i)
    with open('PSI_princ.json','w+') as f:
        json.dump(data,f)
    with open('PSI_t1.json','r+') as f:
        data=json.load(f)
        for i in sma[13:33]:
            data.append(i)
        for i in smb[10:20]:
            data.append(i)
        for i in pc[7:15]:
            data.append(i)
        for i in svt[4:6]:
            data.append(i)
    with open('PSI_t1.json','w+') as f:
        json.dump(data,f)
    with open('PSI_t2.json','r+') as f:
        data=json.load(f)
        for i in sma[33:57]:
            data.append(i)
        for i in smb[20:38]:
            data.append(i)
        for i in pc[15:27]:
            data.append(i)
        for i in svt[6:12]:
            data.append(i)
    with open('PSI_t2.json','w+') as f:
        json.dump(data,f)
    with open('PSI_t3.json','r+') as f:
        data=json.load(f)
        for i in sma[57:85]:
            data.append(i)
        for i in smb[38:50]:
            data.append(i)
        for i in pc[27:37]:
            data.append(i)
    with open('PSI_t3.json','w+') as f:
        json.dump(data,f)

## fonction pour afficher le groupe auquel appartient le bachellier:
def afficher(n):
    with open('PSI_princ.json','r+') as f:
        data1=json.load(f)
    with open('PSI_t1.json','r+') as f:
        data2=json.load(f)
    with open('PSI_t2.json','r+') as f:
        data3=json.load(f)
    with open('PSI_t3.json','r+') as f:
        data4=json.load(f)
    for i in data1:
        if i['Num_ins']==n:
            print('cet candidat appartient au groupe principale')
    for i in data2:
        if i['Num_ins']==n:
            print('cet candidat appartient au groupe Tranche 1')
    for i in data3:
        if i['Num_ins']==n:
            print('cet candidat appartient au graoupe Tranche 2')
    for i in data4:
        if i['Num_ins']==n:
            print('cet candidat appartiene au groupe Tranche 3')

""" partie d'addministration """

# pour remplir la liste des bachellier par l'administration:
 ##  for i in range(int(input('entrer le nmbre total des bachellier pour les enregestrer\n'))):
 ##    student=Bachellier()
 ##   student.saisir()

""" il faut d'abord replir la listes avec les bachelleir avant d'exécuter le reste du code
 sinn sa sert a rien car les fichier vont etre vide
"""
############
### test ###
############

#student=Bachellier()
#formule_Gen()
#classer()
#generer()
#afficher(1111)
