import tkinter as tk
from datetime import datetime

bancodados = "bancodados.txt"
statusinstr = "status.txt"
agora = datetime.now()


def novo_cadastro(codigo, status, usuario, arquivo, arquivostatus):
    escrita = open(arquivo, 'a')
    escrita.write(codigo + ";" + status + ";" + usuario + ";" + str(agora) + ";" + "\n")
    escrita.close()
    substituto = open(arquivostatus, 'r')
    textooriginal = substituto.read()
    a = textooriginal.find(codigo, 0)
    novostatus = textooriginal.replace(codigo + textooriginal[a + 15:a + 54],
                                       codigo + ";" + status + ";" + usuario + ";" + str(agora) + ";")
    substituir = open(arquivostatus, 'w')
    substituir.write(novostatus)
    substituto.close()
    substituir.close()


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.codigo_produto = tk.Text(self, width=20, height=2)  # Caixa de texto para digitar
        self.textoentradasaida = tk.Text(self, width=2, height=2)
        self.textore = tk.Text(self, width=9, height=2)
        self.saidainstr = tk.Button(self)
        self.digitado = tk.Label(self)
        self.labelcodigo = tk.Label(self)
        self.labelentradasaida = tk.Label(self)
        self.labelre = tk.Label(self)
        self.labeladdicionecodigo = tk.Label(self)
        self.quit = tk.Button(self, text="Fechar", fg="red",
                              command=self.master.destroy)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.saidainstr["text"] = "Retirar / Devolver \n instrumento"
        self.codigo_produto.grid(row=0, column=1)
        self.textoentradasaida.grid(row=1, column=1)
        self.textore.grid(row=2, column=1)
        self.saidainstr["command"] = self.saida_instr
        self.labelcodigo["text"] = "Código do instrumento"
        self.labelcodigo.grid(row=0, column=0)
        self.labelentradasaida["text"] = "Entrada / Saída ?"
        self.labelentradasaida.grid(row=1, column=0, pady=22)
        self.labelre["text"] = "R.E. do Colaborador"
        self.labeladdicionecodigo["text"] = "Adicione o código"
        self.labelre.grid(row=2, column=0, pady=22)
        self.labeladdicionecodigo.grid(row=8, column=2)
        self.saidainstr.grid(row=10, column=0, pady=22)
        self.quit.grid(row=10, column=2)

    def saida_instr(self):
        self.digitado.config(text=self.codigo_produto.get(1.0, 1.15))
        codigodigitado = self.codigo_produto.get(1.0, 1.15)
        saidadigitada = self.textoentradasaida.get(1.0, 1.1)
        redigitado = self.textore.get(1.0, 1.8)
        novo_cadastro(codigodigitado, saidadigitada, redigitado, bancodados, statusinstr)
        self.textore.delete(1.0, 2.0)
        self.codigo_produto.delete(1.0, 2.0)
        self.textoentradasaida.delete(1.0, 2.0)
        self.labeladdicionecodigo["text"] = "Saída de instrumento " + codigodigitado + " realizada!"
        print(codigodigitado)


root = tk.Tk()
root.title('Controle de instrumentos')
root.geometry("800x300")
app = Application(master=root)
app.mainloop()
