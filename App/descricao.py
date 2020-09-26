def descricao(nome_arquivo, codigoaserprocurado):
    arquivo = open(nome_arquivo, 'r')
    tabela = arquivo.read()
    tabela = tabela.split(';')
    print(tabela)
    print(codigoaserprocurado == tabela[1])
    if codigoaserprocurado in tabela:
        localiza = list.index(tabela, codigoaserprocurado, 1, list.__len__(tabela))
        print(tabela[localiza] + '\n' + tabela[localiza + 1]
              )
    else:
        print('Código inexistente')
