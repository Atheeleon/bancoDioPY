saldo = 0.0
histDep = []
histSaq = []


def menu():
    print("Qual operação deseja?\n---- 1 - Deposito\n---- 2 - Saque\n---- 3 - Extrato\n---- 0 - Sair")
    match int(input()):
        case 1:
            deposito()
        case 2:
            saque()
        case 3:
            extrato()
        case 0:
            print('Até logo! :)')
            exit()
        case _:
            print('Opção inválida')
            menu()


def deposito():
    global saldo
    dep = float(input('Qual o valor que deseja depositar? '))
    if dep > 0:
        histDep.append(dep)
        saldo += dep
        if input('Deseja realizar outro depósito? (SIM ou NAO)').upper() == 'SIM':
            deposito()
    else:
        print('Você deve inserir um valor válido para deposito.')
        deposito()
    menu()


def saque():
    if len(histDep) == 0:
        print('Não é possível efetuar um saque pois não há saldo.')
        menu()
    elif len(histSaq) < 3:
        global saldo
        saq = float(input('Qual o valor que deseja sacar? '))
        if saq <= saldo and 500 >= saq > 0:
            histSaq.append(saq)
            saldo -= saq
            if input('Deseja realizar outro saque? (SIM ou NAO)').upper() == 'SIM':
                saque()
        else:
            print('Você deve inserir um valor válido para saque.')
            saque()
    else:
        print('Atingido o limite díario para saques.')
    menu()


def extrato():
    if len(histDep) == 0 and len(histSaq) == 0:
        print('Não foram realizadas movimentações.')
    else:
        print('Depositos:')
        for x in histDep:
            print(f'R${x}')

        print('Saques:')
        for x in histSaq:
            print(f'R${x}')

        print(f'Saldo: R${round(saldo, 2)}')
    menu()


print("Olá!")
menu()
