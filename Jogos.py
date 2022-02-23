# Variaveis de cor
branco = '\033[1;30m'
vermelho = '\033[1;31m'
verde = '\033[1;32m'
amarelo = '\033[1;33m'
azul = '\033[1;34m'
roxo = '\033[1;35m'
ciano = '\033[1;36m'
cinza = '\033[1;37m'
semcor = '\033[m'

# Imports
from time import sleep
from random import randint

# Funções
def games():
    print('''{1}ESCOLHA UM {2}GAME{0}{0}
    [{3}1{0}] PEDRA PAPEL OU TESOURA
    [{3}2{0}] ADIVINHE O NÚMERO
    [{3}3{0}] PARA ENCERRAR O PROGRAMA'''.format(semcor,ciano,roxo,branco))
    game = ''
    while game != '3':
        game = input('')
        if game == '1':
            sleep(1.5)
            ppt()
            break
        elif game == '2':
            sleep(1.5)
            an()
            break
        elif game == '3':
            print('{}ENCERRANDO...{}'.format(amarelo,semcor))
            sleep(1.5)
            print('{}PROGRAMA ENCERRADO!{}'.format(vermelho,semcor))
            exit()
        else:
            print('{}OPÇÃO INVALIDA!!!{}'.format(vermelho,semcor))
            sleep(1)
            print('''{1}ESCOLHA UM {2}GAME{0}{0}
            [{3}1{0}] PEDRA PAPEL OU TESOURA
            [{3}2{0}] ADIVINHE O NÚMERO
            [{3}3{0}] PARA ENCERRAR O PROGRAMA'''.format(semcor,ciano,roxo,branco))




def iniciar():
    print('''{1}Você esta pronto para começar o {4}GAME{0}?{0}
    [{2}S{0}] SIM
    [{3}N{0}] NÃO'''.format(semcor,ciano,verde,vermelho,roxo))
    res = ''
    while res != 's' and res != 'n':
        res = input('').lower()
        if res == 's':
            break
        elif res == 'n':
            print('''{1}Escolha uma das opções abaixo:{0}
            [{2}1{0}] Voltar ao menu de {3}GAMES{0}
            [{2}2{0}] Esta pronto para o {3}GAME{0}
            [{2}3{0}] Caso deseja encerrar o programa'''.format(semcor,ciano,branco,roxo))
            subres = ''
            while subres != '3':
                subres = input('')
                if subres == '1':
                    games()
                    break
                elif subres == '2':
                    break
                elif subres == '3':
                    print('{}ENCERRANDO...{}'.format(amarelo,semcor))
                    sleep(1.5)
                    print('{}PROGRAMA ENCERRADO!{}'.format(vermelho,semcor))
                    exit()
                else:   
                    print('{}OPÇÃO INVALIDA!!!{}'.format(vermelho,semcor))
                    sleep(1)
                    print('''{1}Escolha uma das opções abaixo:{0}
                    [{2}1{0}] Voltar ao menu de {3}GAMES{0}
                    [{2}2{0}] Esta pronto para o {3}GAME{0}
                    [{2}3{0}] Caso deseja encerrar o programa'''.format(semcor,ciano,branco,roxo))  
        else:   
            print('{}OPÇÃO INVALIDA!!!{}'.format(vermelho,semcor))
            sleep(1) 
            print('''{1}Você esta pronto para começar o {4}GAME{0}?{0}
            [{2}S{0}] SIM
            [{3}N{0}] NÃO'''.format(semcor,ciano,verde,vermelho,roxo))



# FUNÇÕES DOS GAMES
# Pedra Papel ou Tesoura
def ppt():
    print('{}PEDRA PAPEL OU TESOURA{}'.format(verde,semcor))
    sleep(1.5)
    iniciar()

    print('FIM')
    sleep(2)
    games()

# Adivinhe um número
def an():
    while True:
        print('{}ADIVINHE UM NÚMERO{}'.format(verde,semcor))
        sleep(1.5)
        iniciar()
        print('''{1}ESCOLHA O NIVEL DE DIFICULDADE{0}
        [{2}1{0}] {3}FACIL{0} de 1 a 5 com 3 tentativas
        [{2}2{0}] {4}MEDIO{0} de 1 a 15 com 5 tentativas
        [{2}3{0}] {5}DIFICIL{0} de 1 a 25 com 5 tentativas
        [{2}4{0}] Voltar ao menu de {6}GAMES{0}'''.format(semcor,ciano,branco,verde,amarelo,vermelho,roxo))
        dif = 0
        while dif != 3:
            dif = input('')
            if dif == '1':
                print('{}PENSANDO EM UM NUMERO DE 1 A 5...{}'.format(verde,semcor))
                n = randint(1,5)
                t = 3
                sleep(1.5)
                break
            elif dif == '2':
                print('{}PENSANDO EM UM NUMERO DE 1 A 15...{}'.format(amarelo,semcor))
                n = randint(1,15)
                t = 5
                sleep(1.5)
                break
            elif dif == '3':
                print('{}PENSANDO EM UM NUMERO DE 1 A 25...{}'.format(vermelho,semcor))
                n = randint(1,25)
                t = 5
                sleep(1.5)
                break
            elif dif == '4':
                sleep(1.5)
                games()
                break
            else:
                print('{}OPÇÃO INVALIDA!!!{}'.format(vermelho,semcor))
                sleep(1) 
                print('''{1}ESCOLHA O NIVEL DE DIFICULDADE{0}
                [{2}1{0}] {3}FACIL{0} de 1 a 5 com 3 tentativas
                [{2}2{0}] {4}MEDIO{0} de 1 a 15 com 5 tentativas
                [{2}3{0}] {5}DIFICIL{0} de 1 a 25 com 5 tentativas
                [{2}4{0}] Voltar ao menu de {6}GAMES{0}'''.format(semcor,ciano,branco,verde,amarelo,vermelho,roxo))

        print('{}EM QUAL NUMERO EU PENSEI?{}'.format(azul,semcor))
        nt = 0
        nt2 = t
        for i in range(1,t+1):
            ten = input('')
            nt += 1
            nt2 -= 1
            if ten == str(n):
                print('{}ACERTOU{}'.format(verde,semcor))
                sleep(1)
                print('{}Você usou {} tentativas!{}'.format(azul,nt,semcor))
                break
            else:
                print('{}ERROU{}'.format(vermelho,semcor))
                sleep(1)
                print('{}Você tem mais {} tentativas{}'.format(azul,nt2,semcor))
        print('{1}Parabens! Independente do resultado você {2}ARRASOU!!!{0}{0}'.format(semcor,azul,roxo))
        print('{1}Eu tinha pensado no {2}{3}{0}!{0}'.format(semcor,azul,roxo,n))
        sleep(2)
        print('{}O JOGO IRA REINICIAR EM 5 SEGUNDOS{}'.format(amarelo,semcor))
        sleep(5)

games()
print('Parou tudo')