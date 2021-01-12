from tkinter import *
from tkinter import filedialog

def abrirArquivo():
    arquivo = filedialog.askopenfilename(filetypes = ())

window = Tk()
window.title("ZapBot")
window.geometry('350x500')

botaoAbrir = Button(window, text="Abrir Arquivo", command = abrirArquivo)
botaoAbrir.pack()

window.mainloop()