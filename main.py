saldo = 0.0
histDep = []
histSaq = []
usuarios = []
contas = []


def menu():
    print("Qual operação deseja?"
          "\n---- D - Deposito"
          "\n---- S - Saque"
          "\n---- E - Extrato"
          "\n---- U - Cadastrar Usuário"
          "\n---- C - Criar Conta"
          "\n---- Q - Sair")
    match input().upper():
        case 'D':
            deposito()
        case 'S':
            saque()
        case 'E':
            extrato()
        case 'U':
            cadUser()
        case 'C':
            cadConta()
        case 'Q':
            print('Até logo! :)')
            exit()
        case 'X':
            for x in usuarios:
                print(x)
            for x in contas:
                print(x)
            menu()
        case _:
            print('Opção inválida')
            menu()


def cadUser():
    user = input('Informe seu USUARIO: ')
    cpf = int(input('Informe os numeros do CPF: '))
    key = False

    for x in range(len(usuarios)):
        if usuarios[x]['user'] == user or usuarios[x]['cpf'] == cpf:
            key = True
            break
        else:
            key = False

    if key:
        print('Esse usuário/cpf já está cadastrado')
    else:
        nome = input('Nome completo: ')
        data_nasc = input('Data de nascimento (dd-mm-aaaa): ')
        end = input('Endereço (Logradouro, Numero - Bairro - Cidade/UF): ')
        usuarios.append({'user': user, 'nome': nome, 'data_nasc': data_nasc, 'cpf': cpf, 'end': end})
        print('Usuário cadastrado!')

    menu()


def cadConta():
    cpf = int(input('Informe seu CPF: '))
    key = [] * 2
    for x in range(len(usuarios)):
        if usuarios[x]['cpf'] == cpf:
            print(usuarios[x]['cpf'])
            key = [True, x]
            break
        else:
            key = [False, x + 1]

    if key[0]:
        contas.append({'agencia': '0001', 'num_conta': len(contas) + 1, 'user': usuarios[key[1]]['user']})
        print('Conta criada!')
    else:
        print('Esse usuário não existe!')

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
