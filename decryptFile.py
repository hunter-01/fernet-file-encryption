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

# Definindo arquivo original | Defining original file
arqOriginal = sys.argv[1] #'testeZip.zip'

# Pegando a chave | Taking the key
key = sys.argv[2]#''

#with open('key.txt', 'rb') as file:
#    key = file.read()

# Criando objeto Fernet com a chave | Creating Fernet object with key
fernet = Fernet(key)

# Pegando conteúdo do arquivo original | Getting content from the original file
cOriginal = ''

with open(arqOriginal, 'rb') as file:
    cOriginal = file.read()

# Descriptografando conteúdo | Decrypting content
decrypted = fernet.decrypt(cOriginal)

# Substituindo conteúdo do arquivo original | Replacing original file content
with open(arqOriginal, 'wb') as file:
    file.write(decrypted)

print("Successful decripted")
