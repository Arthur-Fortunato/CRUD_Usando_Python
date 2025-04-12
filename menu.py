from util import entrar_int_nao_negativo

def menu():
    print("[1] - Adicionar pessoa")
    print("[2] - listar pessoas")
    print("[3] - consultar pessoa")
    print("[4] - atualizar pessoa")
    print("[5] - deletar pessoa")
    print("[0] - Sair")

def entrar_opcao():
    menu()
    while (True):
        opt = entrar_int_nao_negativo("Digite o número da lista que deseja: ")
        if((opt >= 0) and (opt <= 5)):
            break
        else:
            print("Erro: valor inválido")
    return opt