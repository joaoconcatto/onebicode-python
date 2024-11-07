import tkinter as tk


# 1- criando a janela
window = tk.Tk()
window.geometry("300x150")
window.title("Gerenciador de frases")


# 2- adicionando o Frame
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill='x', expand=True)


# 3- adicionando o Label
label = tk.Label(frame, text="Hello World")
label.pack(fill="x", expand=True)


# 4- adicionando o input text
frase_lab = tk.Label(frame, text="Frase")
frase_lab.pack(fill="x", expand=True)

frase_inp = tk.Entry(frame)
frase_inp.pack(fill="x", expand=True)


# 5- funcao para alterar o texto da Label
def click():
    label.config(text=frase_inp.get())


# 6- adicionando botao
button = tk.Button(frame, text="Enviar", command=click)
button.pack()

window.mainloop()