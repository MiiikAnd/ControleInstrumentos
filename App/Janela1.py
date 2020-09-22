import tkinter as tk

from App import leitor #  importante ver que App foi a pasta

ler = leitor.encontrar('status.txt', '6.1.001.001.027')

def ler2():
    print(ler)

def say_hi():
    print("hi there, everyone!")


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.hi_there = tk.Button(self)
        self.busca = tk.Button(self)
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there["text"] = "Hello World\n(click me)\nAdicione1"
        self.hi_there["command"] = say_hi
        self.hi_there.pack(side="top")
        self.busca["text"] = "AAA"
        self.busca["command"] = ler2
        self.busca.pack(side="left")
        self.quit.pack(side="bottom")


root = tk.Tk()
root.title('Controle de instrumentos')
root.geometry("800x600")
app = Application(master=root)
app.mainloop()
