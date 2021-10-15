def print_hi(name):
    print(f'Hi, {name}')

def calcular_area_do_retangulo(largura, comprimento):
    return largura*comprimento

def calcular_area_do_quadrado(lado):
    return lado ** 2

def calcular_area_do_triangulo(base, altura):
    return base * altura / 2

def contagem_progressiva(fim):
    for numero in range(fim, 0, -1):
        print(numero)

def apoiar_candidato(vezes, nome):
    for numero in range(vezes):
        print(str(numero+1)+' - '+nome)

def plim(fim):
    for numero in range(fim):
        if (numero+1)%4==0:
            print("PLIM!")
        else:
            print(numero+1)

if __name__ == '__main__':
    continua = True
    while continua:
        print('1 - Imprime o nome.')
        print('2 - Calcula a area do retanguto.')
        print('3 - Calcula a area do quadrado.')
        print('4 - Calcula a area do tringulo.')
        print('5 - Contagem regressiva.')
        print('6 - Apoiar candidato.')
        print('7 - Plim!')
        print('10 - Sair')
        opcao = int(input('Digite sua opcao: '))
        if opcao == 1:
            print_hi('Ricardo')
        elif opcao ==2:
            resultado=calcular_area_do_retangulo(10,20)
            print(f'A área do retangulo é {resultado}m².')
        elif opcao==3:
            resultado = calcular_area_do_quadrado(3)
            print(f'A área do quadrado é {resultado}m².')
        elif opcao==4:
            resultado = calcular_area_do_triangulo(30, 43)
            print(f'A área do triangulo é {resultado}m².')
        elif opcao==5:
            contagem = int(input("Digite o valor da o número da contagem regressiva: "))
            contagem_progressiva(contagem)
        elif opcao==6:
            candidato = input('Nome do candidato: ')
            contagem = int(input('Digite quantas vezes quer apoiar: '))
            apoiar_candidato(contagem, candidato)
        elif opcao==7:
            contagem = int(input('Digite até que número deseja brincar de plim: '))
            plim(contagem)
        elif opcao==10:
            continua=False
        else:
            print('Opção Inválida.')
        print('--------------------------------------------------')