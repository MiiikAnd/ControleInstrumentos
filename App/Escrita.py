from datetime import datetime

agora = datetime.now()
bancodados = "bancodados.txt"
statusinstr = "status2.txt"


def novo_cadastro(codigo, status, usuario, arquivo, arquivostatus):
    escrita = open(arquivo, 'a')
    escrita.write(codigo + ";" + status + ";" + usuario + ";" + str(agora) + ";" + "\n")
    escrita.close()
    substituto = open(arquivostatus, 'r')
    textooriginal = substituto.read()
    a = textooriginal.find(codigo,0)
    novostatus = textooriginal.replace(codigo + textooriginal[a+15:a+50], codigo + ";" + status + ";" + usuario + ";" + str(agora) + ";")
    substituir = open(arquivostatus, 'w')
    substituir.write(novostatus)
    substituto.close()
    substituir.close()


if __name__ == '__main__':
    novo_cadastro("6.1.001.001.027", "D", "2025", bancodados, statusinstr)
