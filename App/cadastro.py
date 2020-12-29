import tkinter as tk
from datetime import datetime

bancodados = "bancodados.txt"
statusinstr = "status.txt"
descricaoinstr = "Instrumentos.txt"


def novo_instrumento(codigo, descricao, statusinic, reinic):
    agora = datetime.now()


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.codigo_produto = tk.Entry(self, width=20, justify='center', xscrollcommand=1)
        self.descricaocodigo = tk.Entry(self, width=100)
        self.reinic = tk.Entry(self, width=9, justify='center', xscrollcommand=1)
        self.statusinic = tk.Entry(self, width=2, justify='center', xscrollcommand=1)
        self.novoinstrumento = tk.Button(self)
        self.lbcodigo = tk.Label(self)
        self.lbcodigo = tk.Label(self)
        self.lbdescricao = tk.Label(self)
        self.lbstatus = tk.Label(self)
        self.lbre = tk.Label(self)
        self.quit = tk.Button(self, text="Fechar", fg="red",
                              command=self.master.destroy)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.novoinstrumento["text"] = "Cadastrar novo\n instrumento"
        self.codigo_produto.grid(row=1, column=0, padx=20)
        self.descricaocodigo.grid(row=1, column=1)
        self.lbcodigo["text"] = "Código do instrumento"
        self.lbcodigo.grid(row=0, column=0)
        self.lbdescricao["text"] = "Descrição"
        self.lbdescricao.grid(row=0, column=1, pady=22)
        self.lbstatus["text"] = "Primeiro status"
        self.lbre["text"] = "R.E."
        self.reinic.grid(row=1, column=3, padx=20)
        self.lbstatus.grid(row=0, column=4)
        self.statusinic .grid(row=1, column=4, padx=20)
        self.lbre.grid(row=0, column=3)
        self.novoinstrumento.grid(row=10, column=0, pady=22)
        self.quit.grid(row=10, column=2)


root = tk.Tk()
root.title('Cadastro de Instrumentos')
root.geometry("1200x300")
app = Application(master=root)
app.mainloop()
