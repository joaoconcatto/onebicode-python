import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title('Cadastro de alunos')


# 1- função para adicionar os dados do estudante:
def add_student():
    name = entry_name.get()
    email = entry_email.get()

    tree.insert('', tk.END, values=(name, email))

    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)


# 2- criando tabela treeview:
tree = ttk.Treeview(root, columns=('Name', 'E-mail'))
tree.heading('Name', text='Name')
tree.heading('E-mail', text='E-mail')
tree.pack()


# 3- criando campos Name:
label_name = tk.Label(root, text='Name')
label_name.pack()
entry_name = tk.Entry(root)
entry_name.pack()


# 4- criando campos E-mail:
label_email = tk.Label(root, text='E-mail')
label_email.pack()
entry_email = tk.Entry(root)
entry_email.pack()


# 5- botao para adicionar aluno:
button_add = tk.Button(root, text='Enviar', command=add_student)
button_add.pack()

root.mainloop()