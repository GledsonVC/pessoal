from tkinter import *
from tkinter import messagebox as mb

# função para abrir showbox informando que irá fechar
def funcaobutao():
        mb.showinfo('Informação', 'Fechar a Aplicação')
        janela.destroy()
# instanciando janela
janela = Tk()

# dimensão da janela
janela.geometry('300x100')

# título da janela
janela.title('Fechar a janela')

# botão Fechar a janela 
botao = Button(janela, text='Fechar a janela', command=funcaobutao)
botao.place(relx=0.35,rely=0.35)

# chamada do loop da janela
janela.mainloop()
