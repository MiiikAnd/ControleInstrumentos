def encontrar(nome_arquivo, item):
    arquivo = open(nome_arquivo, 'r')
    codigo = arquivo.read()
    codigo = codigo.split('\n')
    print(codigo)
    a = item
    if a == codigo[0]:
        print(item)
    else:
        a == codigo[0+1]
        print(item)
    pass
    arquivo.close()


if __name__ == '__main__':
    item = '6.1.001.006.020'
    encontrar('status.txt', item)
