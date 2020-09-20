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


def encontrar(nome_arquivo, item):
    arquivo = open(nome_arquivo, 'r')
    codigo = arquivo.read()
    codigo = codigo.split('\n')
    print(codigo)
    it = codigo.pop(item)
    print(it)
    arquivo.close()


if __name__ == '__main__':
    item = input()
    encontrar('status.txt', int(item))
