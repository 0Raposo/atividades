from tkinter import messagebox
def clicou(altura, peso):
    imc = float(peso)/pow(float(altura), 2 )
    messagebox.showinfo('RESULTADO: ', f'Seu IMC é de: {imc.__round__(2)}')

