from cryptography.fernet import Fernet

# Gerar chave
key = Fernet.generate_key()

# Armazenar chave em arquivo
with open('log-keys.txt', 'ab') as file:
    file.write(key+bytes("\n","utf8"))

# Mostrar key
print("New Key:"+str(key)+"\n Stored in log-keys.txt")