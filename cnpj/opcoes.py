from cnpj import modulos


def opcao_um():
    while True:
        try:
            cnpj = str(input('Digite o CNPJ [somente números]: ')).strip()
        except (TypeError, ValueError):
            print('ERRO! Digite somente números inteiros')
        else:
            if not cnpj.isdigit:
                print('ERRO! Por favor, digite somente números inteiros')
            else:
                cnpj = str(cnpj)  # Fazendo o casting aqui mesmo
                if not len(cnpj) == 14:
                    print('ERRO! Máximo de 14 caracteres')
                elif cnpj[0] * len(cnpj) == cnpj:  # Peguei da correção
                    print('ERRO! Sequências não são permitidas')
                else:
                    break

    cnpj_verificado = modulos.valida_cnpj(cnpj)

    if cnpj == cnpj_verificado:
        print(f'O CNPJ {modulos.pontuacao_cnpj(cnpj)} é válido!')
        print()
        req = modulos.consulta_cnpj(cnpj)
        if not req:
            print('O CNPJ é válido, mas não consta na base da dados da Receita Federal')
        else:
            modulos.printcnpj(req)
    else:
        print('CNPJ inválido!')


def opcao_dois():
    cnpj = modulos.geracnpj()
    return cnpj
