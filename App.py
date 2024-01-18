from Schedule import Schedule

schedule = Schedule()

def menu():
    while True:
        option = input("Cadastro de contatos \n1 - Adicionar contato \n2 - Listar todos os contatos \n3 - Remover todos os contatos \n4 - Sair \n> ")
        match(option):
            case '1':
                name = input("Digite seu nome: ")
                phone = input("Digite seu telefone: ")
                email = input("Digite seu e-mail: ")
                schedule.add_contact(name,phone,email)
            case '2':
                schedule.list_contacts()
            case '3':
                schedule.remove_contacts()
            case '4':
                return False
            case _:
                print("Opção inválida, escolha de 1 a 4")


menu()