import tkinter as tk
from App import atualizador  # importante ver que App foi a pasta

procurado = '6.1.003.002.373'
procurado2 = '6.1.003.002.3721'

a = 'aaaaaaaaaaaaaaaaaaaaaaaaa'
b = 'aaa'
def novo():
    a = atualizador.encontrar('status.txt', procurado)
    print(a)


def say_hi():
    print("hi there, everyone!")


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.descr = tk.Label(self, text=a)
        self.codigo_produto = tk.Text(self, width=20, height=2)  # Caixa de texto para digitar
        self.descricao_produto = tk.Label(self, text="Código do instrumento")  # texto sem nada
        self.buscado = tk.Button(self)
        self.buscado2 = tk.Button(self)
        self.quit = tk.Button(self, text="Fechar", fg="red",
                              command=self.master.destroy)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.buscado["text"] = "item procurado"
        self.buscado2["text"] = "Apagar item"
        self.buscado2["command"] = novo
        self.buscado.grid(row=0, column=0)
        self.buscado2.grid(row=2, column=0)
        self.codigo_produto.grid(row=0, column=2)
        self.descricao_produto.grid(row=1, column=2)
        self.descr.grid(row=1, column=2)
        self.quit.grid(row=10, column=0)




root = tk.Tk()
root.title('Controle de instrumentos')
root.geometry("800x300")
app = Application(master=root)
app.mainloop()
