from tkinter import *

# instancia janela
janela = Tk()
# titulo da janela
janela.title('Titulo da Janela')
# dimensão da janela
janela.geometry('300x100')

# Texto Ola, mundo!
texto_orientacao = Label(janela, text='Ola, mundo!')
texto_orientacao.grid(column=0, row=0, padx=1, pady=10)

# Botão OK para fechar janela
botao = Button(janela, text='   OK  ', command= janela.destroy)
botao.grid(column=0, row=1)

# chama loop para abrir janela
janela.mainloop()
