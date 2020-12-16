from cnpj import modulos, opcoes

print(f'{"=" * 20} CNPJ Online {"=" * 20}')
print()
print('Bem vindo ao validador e gerador de CNPJ')
print()

while True:
    try:
        print('''
    [ 1 ] Consultar CNPJ
    [ 2 ] Gerar CNPJ''')
        opcao = int(input('Digite sua opcão: '))
    
    except (TypeError, ValueError):
        print('ERRO! Digite somente números inteiros')
    
    else:
        if opcao == 1:
            opcoes.opcao_um()

        elif opcao == 2:
            cnpj_gerado = opcoes.opcao_dois()
            print(f'CNPJ Gerado: {cnpj_gerado}')        

        else:
            print('ERRO! Por favor, digite uma opção válida')
