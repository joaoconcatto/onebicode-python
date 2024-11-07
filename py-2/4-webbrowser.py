import webbrowser

done = False

while not done:
    print('O que você deseja fazer?')
    print('1. Aprender Python')
    print('2. Aprender sobre módulos')
    print('3. Aprender Python, Fullstack JS, Inglês e No Code')
    print('4. Sair')

    choice = input('> ')

    if choice == "1":
        webbrowser.open("https://www.python.org/")
    
    elif choice == "2":
        webbrowser.open("https://docs.python.org/pt-br/3/tutorial/modules.html")

    elif choice == "3":
        webbrowser.open("https://comunidade.onebitcode.com/feed")

    elif choice == "4":
        done = True

    else:
        print("Opção inválida...")