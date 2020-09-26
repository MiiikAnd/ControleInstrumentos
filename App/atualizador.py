def encontrar(nome_arquivo, codigoaserprocurado):
    arquivo = open(nome_arquivo, 'r')
    tabela = arquivo.read()
    tabela = tabela.split(';')
    if codigoaserprocurado in tabela:
        localiza = list.index(tabela, codigoaserprocurado, 1, list.__len__(tabela))
        descricao = tabela[localiza +1]
        return descricao
    else:
        print('Código inexistente')


if __name__ == '__main__':
    codigo = '6.1.001.001.027'
    a = encontrar('status.txt', codigo)
    print(a)