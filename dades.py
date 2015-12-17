import os
#Programa que guarda les dades d'un usuari en un fitxer

print("*************Crea un usuari*************")
print("\nIntrodueix les teves dades!\n")

i = input("Indica el nom d'usuari: ")
j = input("Digues el teu nom complet: ")
k = input("Estableix una contrasenya: ")
out = i+":"+j+":"+k

file = open("dades.txt", "w")
file.write(out)
file.close()

print("\n")
os.system("pause")




