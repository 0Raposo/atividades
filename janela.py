from tkinter import *
from tkinter import ttk
from use_cases.funcao import clicou
from tkinter import messagebox


def janelaMain():



    # COMO CRIAR UMA JANELA
    janela = Tk()

    # COMO COLOCAR UM TITULO NA JANELA
    janela.title('CALCULO IMC')

    # LARGURA, ALTURA E POSICIONAMENTO DA JANELA
    janela.geometry('500x500+700+300')


    # CRIANDO UM LABEL
    label_altura = Label(janela, text='ALTURA: ', fg='red', font='Tahoma 16')
    label_peso = Label(janela, text='PESO: ', fg='red', font='Tahoma 16')

    #ADICIONANDO UM WIDGET A JANELA
    label_altura.place(x = 20, y = 10)
    label_peso.place(x = 20, y = 150)

    # ADICIONANDO CAIXA DE TEXTO NA JANELA
    txtAltura = Entry(janela, font='Tahoma 16')
    txtAltura.place(x=20, y=40)

    txtPeso = Entry(janela, font='Tahoma 16')
    txtPeso.place(x=20, y=180)

    #CRIANDO BOTÃO
    btn = Button(janela, text='Enviar', background= 'red', fg = 'white', font= 'Tahoma 17 bold',
                 activebackground= 'white',  activeforeground= 'red', command= lambda: clicou(txtAltura.get(), txtPeso.get()))
    btn.place(x = 20, y = 220 )


    # COMO LIMPAR OS CAMPOS
    txtAltura.delete(0, END)
    txtPeso.delete(0, END)


    # #COMO ALTERAR O TEXTO DE UM LABEL
    # texto = StringVar()
    # txtEnviar = Label(janela, text='', textvariable= texto, fg='red', font='Tahoma 16')
    # txtEnviar.place()


    # COMO EXIBIR A JANELA
    janela.mainloop()