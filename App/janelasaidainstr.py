import tkinter as tk
from App import Escrita  # importante ver que App foi a pasta


bancodados = "bancodados.txt"
statusinstr = "status2.txt"

def say_hi():
    print("hi there, everyone!")


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.codigo_produto = tk.Text(self, width=20, height=2)  # Caixa de texto para digitar
        self.saidainstr = tk.Button(self)
        self.digitado = tk.Label(self)
        self.labelcodigo = tk.Label(self)
        self.labeentradasaida = tk.Label(self)
        self.labelre = tk.Label(self)
        self.quit = tk.Button(self, text="Fechar", fg="red",
                              command=self.master.destroy)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.saidainstr["text"] = "Retirar / Devolver \n instrumento"
        self.codigo_produto.grid(row=0, column=1)
        self.saidainstr["command"] = self.saida_instr
        self.labelcodigo["text"] = "Código"
        self.saidainstr.grid(row=10, column=0)
        self.quit.grid(row=10, column=2)

    def saida_instr(self):
        self.digitado.config(text=self.codigo_produto.get(1.0, 1.15))
        codigodigitado = self.codigo_produto.get(1.0, 1.15)

        Escrita.novo_cadastro(codigodigitado, "E", "2025", bancodados, statusinstr)
        print(codigodigitado)



root = tk.Tk()
root.title('Controle de instrumentos')
root.geometry("800x300")
app = Application(master=root)
app.mainloop()
