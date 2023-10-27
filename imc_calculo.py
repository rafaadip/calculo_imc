import tkinter as tk

def calcular_imc():
    try:
        peso = float(entrada_peso.get())
        altura_cm = float(entrada_altura_cm.get())
        altura_m = altura_cm / 100  # Convertendo altura de cm para m
        imc = peso / (altura_m ** 2)
        resultado_label.config(text=f'Seu IMC é: {imc:.2f}')
    except ValueError:
        resultado_label.config(text='Por favor, insira valores válidos.')


janela = tk.Tk()
janela.title("Calculadora de IMC")
janela.geometry("300x200")

label_peso = tk.Label(janela, text="Peso (kg):")
label_peso.pack()
entrada_peso = tk.Entry(janela)
entrada_peso.pack()

label_altura_cm = tk.Label(janela, text="Altura (cm):")
label_altura_cm.pack()
entrada_altura_cm = tk.Entry(janela)
entrada_altura_cm.pack()


calcular_button = tk.Button(janela, text="Calcular IMC", command=calcular_imc)
calcular_button.pack()

resultado_label = tk.Label(janela, text="")
resultado_label.pack()
janela.mainloop()
