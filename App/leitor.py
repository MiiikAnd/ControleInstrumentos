def ler(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)
    arquivo.close()


def tabela(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    codigo = arquivo.read()
    codigo = codigo.split('\n')
    print(codigo)


def encontrar(nome_arquivo, item, item2):
    arquivo = open(nome_arquivo, 'r')
    codigo = arquivo.read()
    codigo = codigo.split('\n')
    print(codigo)
    print(codigo[item])
    a = item2
    if a == codigo[item]:
        print(item)
    else:
        a == codigo[item+1]
        print(item)
    arquivo.close()


if __name__ == '__main__':
    item = 3
    item2 = '6.1.001.002.024;1'
    encontrar('status.txt', int(item), item2)
