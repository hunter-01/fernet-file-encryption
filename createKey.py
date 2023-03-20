from cryptography.fernet import Fernet

# Gerar chave | Generate key
key = Fernet.generate_key()

# Armazenar chave em arquivo | Store key in file
with open('log-keys.txt', 'ab') as file:
    file.write(key+bytes("\n","utf8"))

# Mostrar key | Show key
print("New Key:"+str(key)+"\n Stored in log-keys.txt")
