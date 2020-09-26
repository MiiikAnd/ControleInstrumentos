def encontrar(nome_arquivo, codigoaserprocurado):
    arquivo = open(nome_arquivo, 'r')
    tabela = arquivo.read()
    tabela = tabela.split(';')
    print(tabela)
    print(codigoaserprocurado == tabela[1])
    if codigoaserprocurado in tabela:
        localiza = list.index(tabela, codigoaserprocurado, 1, list.__len__(tabela))
        print(tabela[localiza] + '\n' + tabela[localiza + 1] +
              '\n' + tabela[localiza + 2] + '\n' + tabela[
            localiza + 3] + '\n' + tabela[localiza + 4])
    else:
        print('Código inexistente')


if __name__ == '__main__':
    codigo = '6.1.001.001.099'
    encontrar('status.txt', codigo)
