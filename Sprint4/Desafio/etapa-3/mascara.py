import hashlib

continua = True 

while continua:
    entrada = input("Digite uma sentença ou 'sair' para encerrar.\n")
    if entrada.strip().lower() == 'sair':
        print('Fechando a aplicação.')
        continua = False
    else:
        cod_hash = hashlib.sha1(entrada.encode())
        print('Hash gerado através da entrada fornecida:')
        print(cod_hash.hexdigest())