# MITM Attack
# Israel Eduardo Hernandez Valdez
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

# Generamos los numeros secretos de Alice, Bob y Eve
sAlice = random.getrandbits(256) #a
sBob = random.getrandbits(256) #b
sEve = random.getrandbits(256) #c

print("\n", "Numero Secreto de Alice: ", sAlice)
print("\n", "Numero Secreto de Bob: ", sBob)
print("\n", "Numero Secreto de Eve: ", sEve)

# Alice manda mensaje a Bob pero es interceptado por Eve
intAlice = pow(g,sAlice,p)
print("\n", "Numero Secreto de Alice a Bob pero interceptado a Eve: ", intAlice)

# Eve le manda mensaje a Bob haciendose pasar por Alice
messEveB = pow(g,sEve,p)
print("\n", "Numero Secreto de Eve haciendose pasar por Alice: ", messEveB)

# Bob manda mensaje a Alice pero es interceptado por Eve
intBob = pow(g,sBob,p)
print("\n", "Numero Secreto de Bob a Alice pero interceptado a Eve: ", intBob)

# Eve le manda mensaje a Alice haciendose pasar por Bob
messEveA = pow(g,sEve,p)
print("\n", "Numero Secreto de Eve haciendose pasar por Bob: ", messEveA)

print("\n", "----------------------")

#Eve calcula la llave secreta compartida por Alice
s1 = pow(messEveA, sEve ,p)
print("\n", "Llave secreta compartida pero Interceptada por Eve: ", s1)

#Eve calcula la llave secreta compartida por Bob
s2 = pow(messEveB, sEve ,p)
print("\n", "Llave secreta compartida por Interceptada por Eve: ", s2)

#Comparamos
h1 = hashlib.sha512(int.to_bytes(s1,length=1024, byteorder='big')).hexdigest()
h2 = hashlib.sha512(int.to_bytes(s2,length=1024, byteorder='big')).hexdigest()

print("\n", "h1: ", h1)
print("\n", "h2: ", h2)


if(h1 == h2):
    print("TRUE", "\n")
else:
    print("FALSE", "\n")