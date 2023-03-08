import socket, time

verde = '\033[0;30;32m'
verde1 = '\033[0;30;42m'
nulo = '\033[0;30;0m'
vermelho = '\033[0;30;31m'
vermelho1 = '\033[0;30;41m'
print('Ex: youtube.com')
a = input('site:')

Portas = [22, 23, 25, 53, 8080, 80, 443, 110, 143, 177]

for Portas in Portas:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.1)
    code = cliente.connect_ex((f'{a}', Portas))
    if code == 0:
        print(f'{verde1}{Portas} OPEN{nulo}')
    elif code == 10035:
        print(f'{vermelho1}{Portas} CLOSED{nulo}')

    elif code == 11:
        print(f'{vermelho1}{Portas} CLOSED{nulo}')
