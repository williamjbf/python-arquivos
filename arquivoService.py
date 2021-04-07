from contato import Contato


def listarContatos():
    listaContatos = list()
    try:
        with open("contatos.txt", "r") as arquivo:
            listaContatosArquivo = arquivo.readlines()
            for i in listaContatosArquivo:
                dados = (i.split('-'))
                contatoArquivo = Contato(dados[0][:-1], dados[1][1:-1], dados[2][1:-1])
                listaContatos.append(contatoArquivo)
        return listaContatos
    except FileNotFoundError:
        print("Arquivo não encontrado")


def buscarContato(emailContato):
    try:
        with open("contatos.txt", "r") as arquivo:
            listaContatos = arquivo.readlines()
            for i, linha in enumerate(listaContatos):
                dados = (linha.split('-'))
                if dados[1][1:-1] == emailContato:
                    return i
            return -1
    except FileNotFoundError:
        print("Arquivo não encontrado")


def buscarContatoEmail(emailContato):
    try:
        linha = buscarContato((emailContato))
        if linha >= 0:
            with open("contatos.txt", "r") as arquivo:
                listaContatos = arquivo.readlines()
                dados = listaContatos[linha].split('-')
                contatoEncontrado = Contato(dados[0][:-1], dados[1][1:-1], dados[2][1:-1])
            return contatoEncontrado
    except FileNotFoundError:
        print("Arquivo não encontrado")


def cadastrarContato(novoContato):
    try:
        if buscarContatoEmail(novoContato.email):
            return False
        else:
            with open("contatos.txt", "a") as arquivo:
                arquivo.write(f"{novoContato.nome} - {novoContato.email} - {novoContato.telefone} \n")
            return True
    except FileNotFoundError:
        print("Arquivo não encontrado")


def removerContatoEmail(emailContato):
    try:
        linha = buscarContato(emailContato)
        if linha >= 0:
            with open("contatos.txt", "r") as arquivo:
                listaContatos = arquivo.readlines()
                contatos = list()
                for i, linhaContato in enumerate(listaContatos):
                    if i != linha:
                        contatos.append(linhaContato)
            with open("contatos.txt", "w") as arquivo:
                arquivo.writelines(contatos)
            return True
        else:
            return False
    except FileNotFoundError:
        print("Arquivo não encontrado")
