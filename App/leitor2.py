def encontrar(nome_arquivo, item):
    arquivo = open(nome_arquivo, 'r')
    codigo = arquivo.read()
    codigo = codigo.split(';')
    print(codigo)
    print(item == codigo[1])
    if item in codigo:
        localiza = list.index(codigo, item, 1, list.__len__(codigo))
        #  Encontra o indice do item procurado
        #  Agumentos: lista, item procurado, inicio da procura, fim da procura(utilizar o list.__len__ para garantir busca a lista toda
        print(codigo[localiza] + '\n' + codigo[localiza+1] + '\n' + codigo[localiza+2] + '\n' + codigo[localiza+3] + '\n'+ codigo[localiza+4])
        a = list.__contains__(codigo, item)  # Se tem na lista retorna true
        b = list.__len__(codigo)  # Quantos itens tem na lista
    else:
        print('Código inexistente')


if __name__ == '__main__':
    item = '6.1.001.001.027'
    encontrar('status.txt', item)
