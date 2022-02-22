import json
import os

rubrica = "rubrica.json"
cestino = "cestino.json"



# SRIVI IN RUBRICA
def Over_write(file_name,ru):
    f = open(file_name, "w")
    f.write(json.dumps(ru)) 
    f.close()


try:
    sizeRub = os.path.getsize(rubrica)
    sizeCess = os.path.getsize(cestino)
except:
    Over_write(rubrica,[])
    Over_write(cestino,[])
    sizeRub = os.path.getsize(rubrica)
    sizeCess = os.path.getsize(cestino)


# STAMPA LA RUBRICA
def Stampa(file):
    f = open(file, "r")
    a = f.read()
    f.close()
    return a


# RICERCA
def Ricerca(index,r,p):
    trov = [False]
    for i in range(0, len(r)):
        if r[i][index] == p:         
            trov[0] = True
            trov.append(i)
    return trov


# MODIFICA
def Mod(index,r,trov):
    print("Inserisci il nuovo "+index)
    x = input()
    a = False
    if index == "telefono":
        a = Ricerca("telefono",r,x)     
        if a[0]:
            print("Telefono già presente")
        else:
            r[trov[1]][index] = x
    else:
        r[trov[1]][index] = x
