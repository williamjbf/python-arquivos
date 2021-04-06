from contato import Contato

print("-" * 30)
print(("-" * 3) + " Agenda de contatos " + ("-" * 3))
print("-" * 30)

opcaoMenu = 1
# listaContatos = list()


while (opcaoMenu != 0):
    print("1. Listar contatos")
    print("2. Cadastrar contato")
    print("3. Remover contato")
    print("4. Buscar contato")
    print("0. Sair")
    opcaoMenu = int(input("Digite a opção desejada: "))

    # if opcaoMenu == 1:
    #     for contatos in listaContatos:
    #         print(f"nome: {contatos.nome} / email: {contatos.email} / telefone: {contatos.telefone}")

    if opcaoMenu == 2:
        try:
            with open("contatos.txt", "a") as arquivo:
                nomeContato = input("Digite o nome do contato: ")
                emailContato = input("Digite o email do contato: ")
                telefoneContato = input("Digite o telefone do contato: ")
                novoContato = Contato(nomeContato, emailContato, telefoneContato)
                arquivo.write(f"{novoContato.nome} - {novoContato.email} - {novoContato.telefone} \n")
            print(arquivo.closed)
        except FileNotFoundError:
            print("Arquivo não encontrado")
        # listaContatos.append(novoContato)

    # elif opcaoMenu == 3:
    #     contatoARemover = input("Digite o email do contato que deseja remover: ")
    #     contatoEncontrado = False
    #     for i in listaContatos:
    #         if i.email == contatoARemover:
    #             listaContatos.remove(i)
    #             print("Contato removido")
    #             contatoEncontrado = True
    #             continue
    #     if not contatoEncontrado:
    #         print("Contato não encontrado")
    #
    # elif opcaoMenu == 4:
    #     buscarContato = input("Digite o email do contato que deseja buscar: ")
    #     contatoEncontrado = False
    #     for i in listaContatos:
    #         if i.email == buscarContato:
    #             print(f"nome: {i.nome} / email: {i.email} / telefone: {i.telefone}")
    #             contatoEncontrado = True
    #             continue
    else:
        print("opcao invalida")
else:
    print("Obrigado por usar a agenda de contatos")
