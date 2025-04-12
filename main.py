from menu import entrar_opcao
from crud import *

pessoas = []

while (True):
    opt = entrar_opcao()
    match(opt):
        case 1:
            adicionar_pessoa(pessoas)
        case 2:
            listar_pessoas(pessoas)
        case 3:
            consultar_pessoa(pessoas)
        case 4:
            atualizar_pessoa(pessoas)
        case 5:
            remover_pessoa(pessoas)
        case 0:
            print("Encerrando o programa...")
            exit()
        case _:
            print("Erro: Valor inválido")