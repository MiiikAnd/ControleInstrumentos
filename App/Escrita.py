from datetime import date, time, datetime, timedelta

agora = datetime.now()
bancodados = "bancodados.txt"
statusinstr = "status.txt"


def novo_cadastro(codigo, status, usuario, arquivo, arquivosta):
    escrita = open(arquivo, 'a')
    escrita.write(codigo + ";" + status + ";" + usuario + ";" + str(agora) + ";" + "\n")
    escrita.close()
    substituto = open(arquivosta, 'r')
    print(substituto.read())
    substituto.close()


if __name__ == '__main__':
    novo_cadastro("6.1.001.002.024", "DISPONIVEL", "2025", bancodados, statusinstr)
