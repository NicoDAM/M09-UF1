from Crypto.Hash import SHA256
import os
#Programa que guarda les dades i el resum d'un usuari en un fitxer

print("*************Crea un usuari*************")
print("\nIntrodueix les teves dades!\n")

iden = input("Indica el nom d'usuari: ")
name = input("Digues el teu nom complet: ")
psw = input("Estableix una contrasenya: ")

obj = SHA256.new(psw.encode('utf-8'))
resum = obj.hexdigest()

output = iden+":"+name+":"+resum
dfile = open("dades+resum.txt", "w")
dfile.write(output)
dfile.close()

print("\n")
os.system("pause")




