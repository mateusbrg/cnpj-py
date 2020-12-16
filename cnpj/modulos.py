import requests
from colorama import Fore
from random import randint


def valida_cnpj(cnpj):
    cnpj_temp = cnpj[:-2]  # Removendo os dois últimos dois caracteres
    multiplicador = 5  # Pra primeira repetição, o multiplicador precisa ser 5
    repeticoes = 0

    while True:
        repeticoes += 1
        d = []  # Lista que salvará os valores das multiplicações e depois somará tudo para a formula final

        for n in cnpj_temp:  # Para cada n (que é uma string) em cnpj_temp
            d.append(int(n) * multiplicador)  # Adiciona na lista o resultado da multiplicação
            if multiplicador == 2:
                multiplicador = 9
                # se for 2, muda pra 9. Tá nessa posição porque o 'n' também tem que multiplicar com 2 antes de mudar
            else:
                multiplicador -= 1

        multiplicador = 6  # Pra segunda repetição, o multiplicador precisa ser 6

        # d = sum(d)
        # Deu um AttributeError porque ao 'd' era atribuído um 'int', e quando o laço While True se repetia pela 2 vez
        # Se mantia com o d == int
        # Resolvi colocando d = [~] no início do While True, para também limpar a lista pros cálculos do próximo dígito
        # AttributeError: 'int' object has no attribute 'append'

        digito = 11 - (sum(d) % 11)
        if digito > 9:
            digito = 0

        cnpj_temp += str(digito)  # Adicionando em cnpj_temp (que é uma string)

        if repeticoes == 2:
            break  # Se já repetiu pros 2 dígitos, interrompe
            # Deu um AttributeError por justamente não fechar o loop infinito
            # AttributeError: 'int' object has no attribute 'append'

    return cnpj_temp


def pontuacao_cnpj(cnpj=''):
    """
    -> O CNPJ é composto de 14 caracteres sendo que os oito primeiros formam o número de inscrição(raiz- nº base),
    os quatro números após a barra representam a quantidades de estabelecimentos inscritos(filiais),
    e os dois últimos algarismos são os dígitos de verificação.

    :param cnpj: CNPJ tipo str
    :return: CNPJ pontuado
    """
    # Lembre que o python não conta o último no fatiamento/range

    raiz = cnpj[:8]
    temp = ''
    for i, n in enumerate(raiz):  # TÁ ERRADO
        temp += n
        if i == 1:
            temp += '.'
        elif i == 4:
            temp += '.'

    raiz = temp

    filiais = cnpj[8:12]
    digitos = cnpj[12:]

    return raiz + '/' + filiais + '-' + digitos


def consulta_cnpj(cnpj):
    r = requests.get(f'https://www.receitaws.com.br/v1/cnpj/{cnpj}')
    req = r.json()

    if req["status"] == 'ERROR':
        return False

    d = {  # Gambiarrinha
        'nome': req["nome"],
        'uf': req["uf"],
        'telefone': req["telefone"],
        'atividade_principal': req["atividade_principal"],
        'situacao': req["situacao"],
        'porte': req["porte"],
        'qsa': req["qsa"],  # Quadro de Sócios e administradores
        # 'qsa' é uma lista, onde cada dicionário dentro da lista é um sócio/administrador
        'bairro': req["bairro"],
        'logradouro': req["logradouro"],
        'numero': req["numero"],
        'cep': req["cep"],
    }
    return d


def printcnpj(req):
    for k, v in req.items():

        if k == 'atividade_principal':
            print(f'{Fore.LIGHTGREEN_EX}{k}: ', end='')
            for i in req["atividade_principal"]:
                print(f'{Fore.YELLOW}{i["text"]}')
            continue

        elif k == 'qsa':
            print()
            print(f'{Fore.LIGHTMAGENTA_EX}LISTA DE SÓCIOS E ADMINISTRADORES{Fore.RESET}')
            for i in req["qsa"]:
                print(f'{Fore.YELLOW}{i["nome"]}')
            print(Fore.RESET)
            continue

        print(f'{Fore.LIGHTGREEN_EX}{k}: {Fore.YELLOW}{v}')
    print(Fore.RESET)


def geracnpj():
    raiz = str(randint(00, 99))
    nbase = str(randint(100000, 999999))
    filial = '0001'
    cnpj = f'{raiz}{nbase}{filial}00'  # 00 para ficar os 14 caracteres certinho
    cnpj = valida_cnpj(cnpj)
    cnpj = pontuacao_cnpj(cnpj)
    return cnpj
