# Practica del Algoritmo de Intercambio de Claves
# Diffe-Helman

import hashlib 
import random 

#numero primo de RFC3526 de 15136 bits - MODP Group
p = int("FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA237327FFFFFFFFFFFFFFFF", 16)
g = 2

# Inicio 
print("\n", "************************")
print("\n", "Variables Publicas Compartidas")
print("\n", "Numeros primos comaprtido publicamente RFC3625: ", p)
print("\n", "Numero base compartido publicamente: ", g)

# Generamos los numeros secretos de Alice y Bob
sAlice = random.getrandbits(256) #a
sBob = random.getrandbits(256) #b

print("\n", "Numero Secreto de Alice: ", sAlice)
print("\n", "Numero Secreto de Bob: ", sBob)

# Alice manda mensaje a Bob -> A = g^a mod p
A = pow(g,sAlice,p)
print("\n", "Numero Secreto de Alice a Bob: ", A)

# Bob manda mensaje a Alice -> B = g^a mod p
B = pow(g,sBob,p)
print("\n", "Numero Secreto de Bob a Alice: ", B)

print("\n", "----------------")

#Alice calcula la llave secreta compartida -> s1 = B^a mod p
s1 = pow(B, sAlice,p)
print("\n", "Llave secreta compartida: ", s1)

#Bob calcula la llave secreta compartida -> s2 = A^b mod p
s2 = pow(A, sBob,p)
print("\n", "Llave secreta compartida: ", s2)

#Comparamos
h1 = hashlib.sha512(int.to_bytes(s1,length=1024, byteorder='big')).hexdigest()
h2 = hashlib.sha512(int.to_bytes(s2,length=1024, byteorder='big')).hexdigest()

print("\n", "h1: ", h1)
print("\n", "h1: ", h2)


if(h1 == h2):
    print("TRUE", "\n")
else:
    print("FALSE", "\n")