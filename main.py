from contato import Contato

print("-" * 30)
print(("-" *3) + " Agenda de contatos " + ("-" *3))
print("-" * 30)

opcaoMenu = 1
listaContatos = list()

while(opcaoMenu != 0):
    print("1. Listar contatos")
    print("2. Cadastrar contato")
    print("0. Sair")
    opcaoMenu = int(input("Digite a opção desejada: "))

    if opcaoMenu == 1:
        for contatos in listaContatos:
            print(f"nome: {contatos.nome} / email: {contatos.email} / telefone: {contatos.telefone}")

    elif opcaoMenu == 2:
        nomeContato = input("Digite o nome do contato: ")
        emailContato = input("Digite o email do contato: ")
        telefoneContato = input("Digite o telefone do contato: ")
        novoContato = Contato(nomeContato, emailContato, telefoneContato)
        listaContatos.append(novoContato)

    else:
        print("opcao invalida")
else:
    print("Obrigado por usar a agenda de contatos TW")
