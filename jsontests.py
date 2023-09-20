import json


def escrever_lista_em_json(lista, nome_arquivo):
    with open(nome_arquivo, "w") as arquivo:
        json.dump(lista, arquivo)


def ler_lista_do_json(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            lista = json.load(arquivo)
        return lista
    except FileNotFoundError:
        return []  # Retorna uma lista vazia se o arquivo não existir
    except json.JSONDecodeError:
        print(f"O arquivo {nome_arquivo} contém um JSON inválido.")
        return []  # Retorna uma lista vazia se o JSON for inválido


def menu():
    print("\nMenu:")
    print("1. Inserir clientes")
    print("2. Editar clientes")
    print("3. Listar clientes")
    print("4. Pesquisar clientes")
    print("5. Sair")


def inserir_cliente(nome_arquivo):
    # Usando um conjunto para garantir nomes únicos
    clientes = set(ler_lista_do_json(nome_arquivo))
    nome = input("Insira o nome do cliente: ")
    clientes.add(nome)
    escrever_lista_em_json(list(clientes), nome_arquivo)
    print(f"Cliente {nome} adicionado.")


def editar_cliente(nome_arquivo):
    clientes = set(ler_lista_do_json(nome_arquivo))
    nome_antigo = input("Insira o nome do cliente a ser editado: ")
    if nome_antigo in clientes:
        nome_novo = input("Insira o novo nome do cliente: ")
        clientes.remove(nome_antigo)
        clientes.add(nome_novo)
        escrever_lista_em_json(list(clientes), nome_arquivo)
        print(f"Cliente {nome_antigo} alterado para {nome_novo}.")
    else:
        print("Cliente não encontrado.")


def listar_clientes(nome_arquivo):
    clientes = ler_lista_do_json(nome_arquivo)
    print("Lista de clientes:")
    for cliente in clientes:
        print(cliente)


def pesquisar_clientes(nome_arquivo, nome):
    clientes = ler_lista_do_json(nome_arquivo)
    if nome in clientes:
        return True
    else:
        return False


arquivo = 'clientes.json'

while True:
    menu()
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Apenas números são permitidos. Tente novamente.")
        continue

    if opcao == 1:
        inserir_cliente(arquivo)
    elif opcao == 2:
        editar_cliente(arquivo)
    elif opcao == 3:
        listar_clientes(arquivo)
    elif opcao == 4:
        nome = input("Insira o nome do cliente a ser pesquisado: ")
        if pesquisar_clientes(arquivo, nome):
            print(f"Cliente {nome} está na lista.")
        else:
            print("Cliente não encontrado.")
    elif opcao == 5:
        print("O programa foi encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")
