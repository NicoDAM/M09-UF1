from Crypto.Hash import SHA256
import os
'''Programa que llegirà les dades d'un fitxer, i comprovarà que l'usuari i contrasenya entrats
són correctes. El document que llegirá será el produït per el fitxer dades+resum.txt'''

print("\n**************Identifica't******************")
print("\nIntrodueix l'usuari i la contrasenya!\n")
false = 1
i = 5

while false == 1:      
    iden = input("Usuari: ")
    psw = input("Contrasenya: ")

    obj = SHA256.new(psw.encode('utf-8'))
    resum = obj.hexdigest()

    file = open("dades+resum.txt", "r")
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
                print("Dades incorrectes!! Torna-ho a intentar! Et queden", i, " intents!\n")
                false = 1

            elif i == 1:
                print("Dades incorrectes!! Torna-ho a intentar! Et queda ", i, " intent!\n")          
                false = 1
                
            else:
                print("Dades incorrectes!! Ja no queden mes intents!!")
                false = 0
    else:
        if i > 1:
            print("Dades incorrectes!! Torna-ho a intentar! Et queden ", i, " intents!\n")
            false = 1
            
        elif i == 1:
            print("Dades incorrectes!! Torna-ho a intentar! Et queda ", i, " intent!\n")          
            false = 1
        else:
            print("Dades incorrectes!! Ja no queden mes intents!!")
            false = 0
    i = i-1    

print("\n")
os.system("pause")
