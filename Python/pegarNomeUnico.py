import sys 
import os

try:
	db = sys.argv[1]
	dl = sys.argv[2]
except Exception:
    #Caso queira mudar a db e o delimitador
	db = "nome.txt"
	dl = " "

f = open(db,'r').readlines()

for i in range(len(f)):
	
    email = f[i].split()[0]
    
    url = "db"+email
    print(email)
    o = open("Aprovadas.txt","a")
    o.write(email+"\n")

#Remover Segundo no ou Sobre nome