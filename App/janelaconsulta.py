import tkinter as tk

bancodados = "bancodados.txt"
statusinstr = "status2.txt"
descricaoinstr = "Instrumentos.txt"
descricao = "aaaa"

def encontrar(nome_arquivo, codigoaserprocurado):
    arquivo = open(nome_arquivo, 'r')
    tabela = arquivo.read()
    tabela = tabela.split(';')
    arquivo.close()
    print(tabela)
    print(codigoaserprocurado == tabela[1])
    if codigoaserprocurado in tabela:
        localiza = list.index(tabela, codigoaserprocurado, 1, list.__len__(tabela))
        descricao = tabela[localiza + 1]
    else:
        descricao = "Código não existe"
        print('Código inexistente')


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.codigo_produto = tk.Text(self, width=20, height=1)  # Caixa de texto para digitar
        self.botaoconsulta = tk.Button(self)
        self.labelcabecalhodescr = tk.Label(self)
        self.labelcabecalhost = tk.Label(self)
        self.labelcabecalhore = tk.Label(self)
        self.labelcabecalhodata = tk.Label(self)
        self.labeldescr = tk.Label(self)
        self.labelstatus = tk.Label(self)
        self.labelre = tk.Label(self)
        self.labeldata = tk.Label(self)
        self.quit = tk.Button(self, text="Fechar", fg="red",
                              command=self.master.destroy)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.botaoconsulta["text"] = "Consultar"
        self.codigo_produto.grid(row=0, column=1)
        self.botaoconsulta["command"] = self.saida_instr
        self.labelcabecalhodescr["text"] = "Descrição"
        self.labelcabecalhodescr.grid(row=2, column=0, pady=20)
        self.labeldescr["text"] = ""
        self.labeldescr.grid(row=3, column=0, pady=20)
        self.labelcabecalhost["text"] = "Status"
        self.labelcabecalhost.grid(row=2, column=1, pady=20)
        self.labelstatus["text"] = ""
        self.labelstatus.grid(row=3, column=1, pady=20)
        self.labelcabecalhore["text"] = "R.E."
        self.labelcabecalhore.grid(row=2, column=3, pady=20)
        self.labelre["text"] = ""
        self.labelre.grid(row=3, column=3, pady=20)
        self.labelcabecalhodata["text"] = "Data"
        self.labelcabecalhodata.grid(row=2, column=4, pady=20)
        self.labeldata["text"] = ""
        self.labeldata.grid(row=3, column=4, pady=20)
        self.botaoconsulta.grid(row=10, column=0, pady=22)
        self.quit.grid(row=10, column=2)

    def saida_instr(self):
        codigodigitado = self.codigo_produto.get(1.0, 1.15)
        encontrar(descricaoinstr, codigodigitado)
        self.labeldescr["text"] = descricao
        self.labelstatus["text"] = codigodigitado
        self.labelre["text"] = codigodigitado
        self.labeldata["text"] = codigodigitado
        print(codigodigitado)


root = tk.Tk()
root.title('Controle de instrumentos')
root.geometry("800x300")
app = Application(master=root)
app.mainloop()
