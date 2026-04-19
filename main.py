from tkinter import *
from tkinter import ttk

cor00 = "#000000"
cor01 = "#666a78"

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(background=cor00)

frameTela = Frame(janela, width=235, height=50, background=cor01)
frameTela.grid(row=0, column=0)

frameCorpo = Frame(janela, width=235, height=268)
frameCorpo.grid(row=1, column=0)


janela.mainloop()