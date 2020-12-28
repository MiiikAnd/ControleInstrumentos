import tkinter as tk

bancodados = "bancodados.txt"
statusinstr = "status.txt"
descricaoinstr = "Instrumentos.txt"


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.codigo_produto = tk.Entry(self, width=20)  # Caixa de texto para digitar
        self.botaoconsulta = tk.Button(self)
        self.labelcabecalhodescr = tk.Label(self)
        self.labelcabecalhost = tk.Label(self)
        self.labelcabecalhore = tk.Label(self)
        self.labelcabecalhodata = tk.Label(self)
        self.labeldescr = tk.Label(self)
        self.labelstatus = tk.Label(self)
        self.labelre = tk.Label(self)
        self.labeldata = tk.Label(self)
        self.labelcodigo = tk.Label(self)
        self.quit = tk.Button(self, text="Fechar", fg="red",
                              command=self.master.destroy)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.botaoconsulta["text"] = "Consultar"
        self.codigo_produto.grid(row=0, column=1)
        self.botaoconsulta["command"] = self.consulta_instr
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
        self.labelre.grid(row=3, column=3, pady=40)
        self.labelcabecalhodata["text"] = "Data"
        self.labelcabecalhodata.grid(row=2, column=4, pady=20)
        self.labeldata["text"] = ""
        self.labeldata.grid(row=3, column=4, pady=20)
        self.labelcodigo["text"] = ""
        self.labelcodigo.grid(row=4, column=0, pady=20)
        self.botaoconsulta.grid(row=10, column=0, pady=22)
        self.quit.grid(row=10, column=2)

    def consulta_instr(self):
        codigodigitado = self.codigo_produto.get()
        arquivodescr = open(descricaoinstr, 'r')
        tabela = arquivodescr.read()
        tabela = tabela.split(';')
        arquivodescr.close()
        localiza = list.index(tabela, codigodigitado, 1, list.__len__(tabela))
        descricao = tabela[localiza + 1]
        self.labeldescr["text"] = descricao
        arquivostatus = open(statusinstr, 'r')
        tabelastatus = arquivostatus.read()
        tabelastatus = tabelastatus.split(';')
        arquivostatus.close()
        localizastatus = list.index(tabelastatus, codigodigitado, 1, list.__len__(tabelastatus))
        status = tabelastatus[localizastatus + 1]
        re = tabelastatus[localizastatus + 2]
        data = tabelastatus[localizastatus + 3]
        self.labelstatus["text"] = status
        self.labelre["text"] = re
        self.labeldata["text"] = data
        self.labelcodigo["text"] = codigodigitado


root = tk.Tk()
root.title('Controle de instrumentos')
root.geometry("800x400")
app = Application(master=root)
app.mainloop()
