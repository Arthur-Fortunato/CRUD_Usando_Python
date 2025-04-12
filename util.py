def entrar_int_nao_negativo(msg):
    while (True):
        try:
            num = int(input(msg))
            if(num >= 0):
                break
            else:
                print("Erro: Digite um valor maior ou igual a zero")
        except:
            print("Erro: valor inválido")
    return num

def entrar_id(lista):
    idx = entrar_int_nao_negativo("Digite o número da lista que corresponde a pessoa que deseja consultar: ")
    if((idx < 0) or (idx >= len(lista))):
        print("Pessoa não encontrada.")
        return
    return idx

def verificar_lista_vazia(lista):
    if (not lista):
        print("A lista está vazia.")
        return True
    return False