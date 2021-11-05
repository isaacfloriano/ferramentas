import os

print("""
 /$$   /$$ /$$$$$$$$ /$$      /$$ /$$$$$$$$  /$$$$$$  /$$   /$$
| $$$ | $$| $$_____/| $$  /$ | $$|__  $$__/ /$$__  $$| $$$ | $$
| $$$$| $$| $$      | $$ /$$$| $$   | $$   | $$  \ $$| $$$$| $$
| $$ $$ $$| $$$$$   | $$/$$ $$ $$   | $$   | $$  | $$| $$ $$ $$
| $$  $$$$| $$__/   | $$$$_  $$$$   | $$   | $$  | $$| $$  $$$$
| $$\  $$$| $$      | $$$/ \  $$$   | $$   | $$  | $$| $$\  $$$
| $$ \  $$| $$$$$$$$| $$/   \  $$   | $$   |  $$$$$$/| $$ \  $$
|__/  \__/|________/|__/     \__/   |__/    \______/ |__/  \__/
                                                               
Sobre:
    Ferramenta para filtra texto.
Manual:
    Sua Database deve está dentro de lista.txt
    O resultado estará dentro de filtro.txt
""")

try:
	db = sys.argv[1]
	dl = sys.argv[2]
except Exception:
	db = "lista.txt"
	dl = "|" 

f = open(db,'r').readlines()

for i in range(len(f)):
	
    email = f[i].split()[0].split(dl)[0]
    senha = f[i].split()[0].split(dl)[1]
    
    #print(email+dl+senha)
    o = open("filtro.txt","a")
    o.write(email+dl+senha+"\n")

print("Pronto!")