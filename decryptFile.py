import sys
from cryptography.fernet import Fernet

if len(sys.argv) <= 1:
    print("No enough arguments")
    exit()

if sys.argv[1] == None:
    print("No File")
    exit()

if sys.argv[2] == None:
    print("No Key")
    exit()

# Definindo arquivo original
arqOriginal = sys.argv[1] #'testeZip.zip'

# Pegando a chave
key = sys.argv[2]#''

#with open('key.txt', 'rb') as file:
#    key = file.read()

# Criando objeto Fernet com a chave
fernet = Fernet(key)

# Pegando conteúdo do arquivo original
cOriginal = ''

with open(arqOriginal, 'rb') as file:
    cOriginal = file.read()

# Descriptografando conteúdo
decrypted = fernet.decrypt(cOriginal)

# Substituindo conteúdo do arquivo original
with open(arqOriginal, 'wb') as file:
    file.write(decrypted)

print("Successful decripted")
