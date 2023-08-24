# Projeto Agenda Telefônica

agenda = {
    "Leticia": "85 99999-9998",
    "Matheus": "88 98989-3333"

}
def adicionarContato(nome: str, telefone: str) -> None:
    if nome in agenda:
        print("Contato já existente! Numero não adicionado")
    else:
        agenda[nome] = telefone
        print("Contato adicionado com sucesso!")

def editarContato(nome: str, telefone: str) -> None:
    if nome in agenda:
        agenda[nome] = telefone
        print("Contato alterado com sucesso!")
    else:
        print("Contato não existe!")

def buscarContato(nome: str) -> None:
    if nome in agenda:
        print(f"Contato: {nome} \n"
        f"Telefone: {agenda[nome]}")
    else:
        print("Contato não existe!")

def deletarContato(nome: str) -> None:
    if nome in agenda:
        del agenda[nome]
        print(f"Contato excluido!")
    else:
        print("Contato não existe!")

def listarTodos() -> None:
    print(agenda)
    print("*****************************")


while True:
    print("----- Agenda Telefonica -----")
    opcao = int(input("1 - Adicionar Contato\n"
                      "2 - Editar Contato\n"
                      "3 - Buscar Contato \n"
                      "4 - Deletar Contato\n"
                      "5 - Listar Todos\n"
                      "6 - Sair\n"
                      "Selecione uma opção: "))
    if opcao == 1:
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone: ")
        adicionarContato(nome, telefone)

    elif opcao == 2:
        nome = input("Qual contato deseja editar? ")
        telefone = input("Qual o novo telefone? ")
        editarContato(nome, telefone)

    elif opcao == 3:
        nome = input("Qual o contato? ")
        buscarContato(nome)

    elif opcao == 4:
        nome = input("Qual o contato? ")
        deletarContato(nome)

    elif opcao == 5:
        listarTodos()

    elif opcao == 6:
        break

    else:
        print("Opção Invalida")
