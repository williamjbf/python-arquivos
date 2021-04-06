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

    if opcaoMenu == 1:
        try:
            with open("contatos.txt", "r") as arquivo:
                listaContatos = arquivo.readlines()
                for i in listaContatos:
                    dados = (i.split('-'))
                    novoContato = Contato(dados[0][:-1], dados[1][1:-1], dados[2][1:-1])
                    print(f"nome: {novoContato.nome} | email: {novoContato.email} | telefone: {novoContato.telefone}")
        except:
            print("Arquivo não encontrado")

    elif opcaoMenu == 2:
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

    elif opcaoMenu == 3:
        try:
            contatoARemover = input("Digite o email do contato que deseja remover: ")
            contatoEncontrado = False
            with open("contatos.txt", "r") as arquivo:
                listaContatos = arquivo.readlines()
                contatos = list()
                for i in listaContatos:
                    dados = (i.split('-'))
                    if dados[1][1:-1] == contatoARemover:
                        contatoEncontrado = True
                    if dados[1][1:-1] != contatoARemover:
                        contatos.append(f"{dados[0]}-{dados[1]}-{dados[2]}")
            with open("contatos.txt", "w") as arquivo:
                arquivo.writelines(contatos)
            if not contatoEncontrado:
                print("Contato não encontrado")
        except:
            print("Arquivo não encontrado")
    elif opcaoMenu == 4:
        try:
            buscarContato = input("Digite o email do contato que deseja buscar: ")
            contatoEncontrado = False
            with open("contatos.txt", "r") as arquivo:
                listaContatos = arquivo.readlines()
                for i in listaContatos:
                    dados = (i.split('-'))
                    if dados[1][1:-1] == buscarContato:
                        novoContato = Contato(dados[0][:-1], dados[1][1:-1], dados[2][1:-1])
                        print(
                            f"nome: {novoContato.nome} | email: {novoContato.email} | telefone: {novoContato.telefone}")
                        contatoEncontrado = True
                        break
            if not contatoEncontrado:
                print("Contato não encontrado")
        except FileNotFoundError:
            print("Arquivo não encontrado")

    else:
        print("opcao invalida")

else:
    print("Obrigado por usar a agenda de contatos")
