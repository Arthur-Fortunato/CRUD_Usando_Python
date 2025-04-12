from util import *

def adicionar_pessoa(pessoas):
    nome = input("Digite o nome da pessoa que será adicionada: ")
    idade = entrar_int_nao_negativo("Digite a idade dessa pessoa: ")
    telefone = input("Digite o telefone dessa pessoa: ")
    pessoas.append([nome, idade, telefone])
    print(f"{nome} foi adicionado com sucesso!")

def listar_pessoas(pessoas):
    if (not pessoas):
        print("Nenhuma pessoa está na lista.")
    for i, pessoa in enumerate(pessoas):
        print(f"{i}. Nome: {pessoa[0]} | Idade: {pessoa[1]} | Telefone: {pessoa[2]}")

def consultar_pessoa(pessoas):
    if (verificar_lista_vazia(pessoas)):
        return
    listar_pessoas(pessoas)
    idx = entrar_id(pessoas)
    if (idx is None):
        return
    pessoa = pessoas[idx]
    print(f"Nome: {pessoa[0]} | Idade: {pessoa[1]} | CPF: {pessoa[2]}")

def atualizar_pessoa(pessoas):
    if (verificar_lista_vazia(pessoas)):
        return
    listar_pessoas(pessoas)
    idx = entrar_id(pessoas)
    pessoa = pessoas[idx]
    novo_nome = input("Digite o novo nome: ")
    nova_idade = entrar_int_nao_negativo("Digite a nova idade: ")
    novo_telefone = input("Digite o novo telefone: ") 
    pessoa[0] = novo_nome
    pessoa[1] = nova_idade
    pessoa[2] = novo_telefone
    print(f"Nome atualizado: {pessoa[0]} | idade atualizada: {pessoa[1]} | novo telefone: {pessoa[2]}")

def remover_pessoa(pessoas):
    if (verificar_lista_vazia(pessoas)):
        return
    listar_pessoas(pessoas)
    idx = entrar_id(pessoas)
    pessoa = pessoas[idx]
    pessoas.remove(pessoa)
    print(f"A pessoa com o ID: {idx} foi removida com sucesso!")