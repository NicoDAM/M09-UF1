from Crypto.Hash import SHA256
import os
#Els pasos anteriors units

print("*************Crea un usuari*************")
print("\nIntrodueix les teves dades!\n")

iden = input("Indica el nom d'usuari: ")
name = input("Digues el teu nom complet: ")
psw = input("Estableix una contrasenya: ")

obj = SHA256.new(psw.encode('utf-8'))
resum = obj.hexdigest()

output = iden+":"+name+":"+resum
dfile = open("usuari.txt", "w")
dfile.write(output)
dfile.close()

print("\n**************Identifica't******************")
print("\nIntrodueix l'usuari i la contrasenya!\n")

false = 1
i = 5

while false == 1:      

    iden = input("Usuari: ")
    psw = input("Contrasenya: ")

    obj = SHA256.new(psw.encode('utf-8'))
    resum = obj.hexdigest()

    file = open("usuari.txt", "r")
    dades = file.readlines()
    file.close()

    line = dades[0]
    line = line.split(":")
    iden1 = line[0]
    resum1 = line[2]

    if iden == iden1:
        if resum == resum1:
            print("\nCorrecte!!")
            false = 0
        else:
            if i > 1:
                print("Dades incorrectes!! Torna-ho a intentar! Et queden ", i ," intents!\n")
                false = 1
            elif i == 1:
                print("Dades incorrectes!! Torna-ho a intentar! Et queda ", i ," intent!\n")          
                false = 1
            else:
                print("Dades incorrectes!! Ja no queden mes intents!!")
                false = 0
    else:
        if i > 1:
            print("Dades incorrectes!! Torna-ho a intentar! Et queden ", i ," intents!\n")
            false = 1
        elif i == 1:
            print("Dades incorrectes!! Torna-ho a intentar! Et queda ", i ," intent!\n")          
            false = 1
        else:
            print("Dades incorrectes!! Ja no queden mes intents!!")
            false = 0
    i = i-1

print("\n")
os.system("pause")
