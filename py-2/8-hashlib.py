import hashlib

# 1- Verificar os algoritmos disponíveis
print(hashlib.algorithms_available)


# 2- Algoritmos disponíveis de acordo com o SO
print(hashlib.algorithms_guaranteed)


# 3- Utilizando sha256
algorithm = hashlib.sha256()
message = "A chave de segurança do servidor é INTERJG08".encode()
algorithm.update(message)
print(algorithm.hexdigest())


# 4- Utilizando MD5
md5 = hashlib.md5()
md5.update(message)
print(md5.hexdigest())
