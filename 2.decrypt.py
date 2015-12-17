from Crypto.Cipher import AES
#decodificar imatge a partir de bytes
fitxer_in=open("images.enc",'rb')    #arxiu del que agafarem les dades
fitxer_dec=open("images1.jpg", 'wb')    #arxiu on es guardaran les dades

clau = b"1234567891012345"   #clau publica
iv = b"1111111111111111"    #clau privada

obj = AES.new(clau, AES.MODE_CBC, iv) #creació del objecte en el que es realitzara la encriptcaió

while True:
    bloc=fitxer_in.read (8192) #llegeix en blocs de  bytes
    if not bloc:    #Per afegir quan finalitza la condició.
        break
    lon=len(bloc) #calcula la logitud del bloc.
    num=lon%16  # Calcula el residu de la longitud del bloc entre 16
    
    if num >0:
        padding=16-num
        bloc+=b'0'*padding  #calcula el numero de 0 que s'han d'afegir per a crear els blocs de 16 bytes.

    enc=obj.decrypt (bloc)   #indicar si es encrypt o decrypt
    fitxer_dec.write (enc)

fitxer_in.close()
fitxer_dec.close()


