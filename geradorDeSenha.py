from pyperclip import copy
import random
import string

senhaGerada = []
conti = ''
guardado = []
arq = 's3nhas.txt'

try:
    with open(arq) as f:
        pass
except FileNotFoundError:
    with open(arq, 'w') as f:
        pass

while conti != 'N':
    senhaGerada.clear()
    quant = int(input('Quantidade de letras para senha: '))
    print('==' * 10)
    print('[1] letras\n[2] números\n[3] números e letras')
    print('==' * 10)
    while True:
        try:
            letr_num = int(input('Escolha um número entre 1 e 3: '))
            if letr_num < 1 or letr_num > 3:
                print('Número inválido! Tente novamente.')
            else:
                break

        except ValueError:
            print('Entrada Invalida! Tente novamente.')

    sinai = str(input('Sinais [S/N]: ')).upper().strip()

    if letr_num == 1:
        if sinai in 'S':
            for c in range(quant):
                senhaGerada.append(random.choice(string.ascii_letters + string.punctuation))
        else:
            for c in range(quant):
                senhaGerada.append(random.choice(string.ascii_letters))

    if letr_num == 2:
        if sinai in 'S':
            for c in range(quant):
                senhaGerada.append(random.choice(string.digits + string.punctuation))
        else:
            for c in range(quant):
                senhaGerada.append(random.choice(string.digits))

    if letr_num == 3:
        if sinai in 'S':
            for c in range(quant):
                senhaGerada.append(random.choice(string.ascii_letters + string.digits + string.punctuation))
        else:
            for c in range(quant):
                senhaGerada.append(random.choice(string.ascii_letters + string.digits))

    senha = ''.join(senhaGerada)
    print(senha)

    guardado.append(senha)

    salva = str(input('Quer salvar a senha? [S/N]: ')).upper().strip()
    if salva in 'S':
        utizaSenha = str(input('Você vai utilizar a senha onde? '))
        copy(senha)
        try:
            with open('s3nhas.txt', 'a') as arq:
                arq.write('\nNome: ' + utizaSenha + '\nSenha: ' + ''.join(guardado))
        except FileNotFoundError:
            print('Arquivo não encontrado!')
        except PermissionError:
            print('Sem permissão para escrever no arquivo!')

    conti = str(input('Quer continuar? [S/N]: ')).upper().strip()

print('\033[1;33mBoa Sorte\033[m :>')