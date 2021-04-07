from arquivoService import *

print("-" * 30)
print(("-" * 3) + " Agenda de contatos " + ("-" * 3))
print("-" * 30)

opcaoMenu = 1

while (opcaoMenu != 0):
    print("1. Listar contatos")
    print("2. Cadastrar contato")
    print("3. Remover contato")
    print("4. Buscar contato")
    print("0. Sair")
    opcaoMenu = int(input("Digite a opção desejada: "))

    if opcaoMenu == 1:
        contatos = listarContatos()
        for contato in contatos:
            print(f"nome: {contato.nome} | email: {contato.email} | telefone: {contato.telefone}")

    elif opcaoMenu == 2:
        nomeContato = input("Digite o nome do contato: ")
        emailContato = input("Digite o email do contato: ")
        telefoneContato = input("Digite o telefone do contato: ")
        novoContato = Contato(nomeContato, emailContato, telefoneContato)
        if cadastrarContato(novoContato):
            print("Contato cadastrado com sucesso")
        else:
            print("Contato já cadastrado")
    elif opcaoMenu == 3:
        contatoARemover = input("Digite o email do contato que deseja remover: ")
        contatoRemovido = removerContatoEmail(contatoARemover)
        if contatoRemovido:
            print("Contato removido com sucesso")
        else:
            print("Contato não encontrado")
    elif opcaoMenu == 4:
        buscarContato = input("Digite o email do contato que deseja buscar: ")
        contatoEncontrado = buscarContatoEmail(buscarContato)
        if contatoEncontrado:
            print(f"nome: {contatoEncontrado.nome} | email: {contatoEncontrado.email} | telefone: {contatoEncontrado.telefone}")
        else:
            print("Contato não encontrado")
    else:
        print("opcao invalida")

else:
    print("Obrigado por usar a agenda de contatos")
