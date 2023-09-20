
listaEstudantes = []
listaProfessores = []
listaDisciplinas = []
listaTurmas = []
listaMatriculas = []


def menu_principal():
    print('\n\n----- MENU PRINCIPAL -----\n')
    print('(1) Gerenciar estudantes.')
    print('(2) Gerenciar professores.')
    print('(3) Gerenciar disciplinas.')
    print('(4) Gerenciar turmas.')
    print('(5) Gerenciar matrículas.')
    print('(9) Sair.\n')

# INCLUIR ENTIDADES


def incluir_estudante():
    print("\n\n===== INCLUSÃO DE ESTUDANTE =====\n")
    codigo = int(input('Insira o código do estudante:\n'))
    nome = input('Insira o nome do estudante:\n')
    estudante = {"Código": codigo, "Nome": nome}
    listaEstudantes.append(estudante)
    input('Estudante Adicionado! \nPressione ENTER para continuar\n')


def incluir_professor():
    print("\n\n===== INCLUSÃO DE PROFESSOR =====\n")
    codigo = int(input('Insira o código do professor:\n'))
    nome = input('Insira o nome do professor:\n')
    cpf = input('Insira o CPF do professor:\n')
    professor = {"Código": codigo, "Nome": nome, "CPF": cpf}
    listaProfessores.append(professor)
    input('Professor Adicionado! \nPressione ENTER para continuar\n')


def incluir_disciplina():
    print("\n\n===== INCLUSÃO DE DISCIPLINA =====\n")
    codigo = int(input('Insira o código da disciplina:\n'))
    nome = input('Insira o nome da disciplina:\n')
    disciplina = {"Código": codigo, "Nome": nome}
    listaDisciplinas.append(disciplina)
    input('Disciplina Adicionada! \nPressione ENTER para continuar\n')


def incluir_turma():
    print("\n\n===== INCLUSÃO DE TURMA =====\n")
    codigo_turma = int(input('Insira o código da turma:\n'))
    codigo_professor = int(input('Insira o código do professor da turma:\n'))
    codigo_disciplina = int(input('Insira o código da disciplina da turma:\n'))

    # Verificar duplicatas de código de turma
    if any(turma['Código'] == codigo_turma for turma in listaTurmas):
        print(f'Já existe uma turma com o código {codigo_turma}.')
    else:
        turma = {"Código": codigo_turma, "Código do Professor": codigo_professor,
                 "Código da Disciplina": codigo_disciplina}
        listaTurmas.append(turma)
        input('Turma Adicionada! \nPressione ENTER para continuar\n')


def incluir_matricula():
    print("\n\n===== INCLUSÃO DE MATRÍCULA =====\n")
    codigo_turma = int(input('Insira o código da turma da matrícula:\n'))
    codigo_estudante = int(
        input('Insira o código do estudante da matrícula:\n'))

    # Verificar duplicatas de código de matrícula
    if any(matricula['Código da Turma'] == codigo_turma and matricula['Código do Estudante'] == codigo_estudante for
           matricula in listaMatriculas):
        print(f'Já existe uma matrícula com esses códigos.')
    else:
        matricula = {"Código da Turma": codigo_turma,
                     "Código do Estudante": codigo_estudante}
        listaMatriculas.append(matricula)
        input('Matrícula Adicionada! \nPressione ENTER para continuar\n')

# LISTAR ENTIDADES


def listar_estudantes():
    print("\n\n===== LISTAGEM DE ESTUDANTES =====\n")
    if len(listaEstudantes) < 1:
        print('Não foram encontrados estudantes.')
    else:
        for i, estudante in enumerate(listaEstudantes, start=1):
            print(
                f"{i}. Código: {estudante['Código']}, Nome: {estudante['Nome']}")


def listar_professores():
    print("\n\n===== LISTAGEM DE PROFESSORES =====\n")
    if len(listaProfessores) < 1:
        print('Não foram encontrados professores.')
    else:
        for i, professor in enumerate(listaProfessores, start=1):
            print(
                f"{i}. Código: {professor['Código']}, Nome: {professor['Nome']}, CPF: {professor['CPF']}")


def listar_disciplinas():
    print("\n\n===== LISTAGEM DE DISCIPLINAS =====\n")
    if len(listaDisciplinas) < 1:
        print('Não foram encontradas disciplinas.')
    else:
        for i, disciplina in enumerate(listaDisciplinas, start=1):
            print(
                f"{i}. Código: {disciplina['Código']}, Nome: {disciplina['Nome']}")


def listar_turmas():
    print("\n\n===== LISTAGEM DE TURMAS =====\n")
    if len(listaTurmas) < 1:
        print('Não foram encontradas turmas.')
    else:
        for i, turma in enumerate(listaTurmas, start=1):
            print(
                f"{i}. Código da Turma: {turma['Código']}, Código do Professor: {turma['Código do Professor']}, Código da Disciplina: {turma['Código da Disciplina']}")


def listar_matriculas():
    print("\n\n===== LISTAGEM DE MATRÍCULAS =====\n")
    if len(listaMatriculas) < 1:
        print('Não foram encontradas matrículas.')
    else:
        for i, matricula in enumerate(listaMatriculas, start=1):
            print(
                f"{i}. Código da Turma: {matricula['Código da Turma']}, Código do Estudante: {matricula['Código do Estudante']}")


# ATUALIZAR ENTIDADES

def atualizar_estudante():
    print("\n\n===== ATUALIZAÇÃO DE ESTUDANTE =====\n")
    if len(listaEstudantes) < 1:
        print('Não há estudantes para atualizar')
    else:
        for i, estudante in enumerate(listaEstudantes):
            print(
                f"{i + 1}. Código: {estudante['Código']}, Nome: {estudante['Nome']}")
        try:
            indice_edicao = int(
                input('Informe o número do estudante que deseja editar: ')) - 1

            if 0 <= indice_edicao < len(listaEstudantes):
                novo_nome = input('Insira o novo nome do estudante: ')
                listaEstudantes[indice_edicao]['Nome'] = novo_nome
                print(
                    f'O estudante foi atualizado para "{novo_nome}" com sucesso.')
            else:
                print('Número de estudante inválido.')
        except ValueError:
            print('Número inválido. Certifique-se de digitar um número válido.')


def atualizar_professor():
    print("\n\n===== ATUALIZAÇÃO DE PROFESSOR =====\n")
    if len(listaProfessores) < 1:
        print('Não há professores para atualizar.')
    else:
        for i, professor in enumerate(listaProfessores):
            print(
                f"{i + 1}. Código: {professor['Código']}, Nome: {professor['Nome']}, CPF: {professor['CPF']}")
        try:
            indice_edicao = int(
                input('Informe o número do professor que deseja editar: ')) - 1

            if 0 <= indice_edicao < len(listaProfessores):
                novo_nome = input('Insira o novo nome do professor: ')
                novo_cpf = input('Insira o novo CPF do professor: ')
                listaProfessores[indice_edicao]['Nome'] = novo_nome
                listaProfessores[indice_edicao]['CPF'] = novo_cpf
                print(
                    f'O professor foi atualizado para "{novo_nome}" com sucesso.')
            else:
                print('Número de professor inválido.')
        except ValueError:
            print('Número inválido. Certifique-se de digitar um número válido.')


def atualizar_disciplina():
    print("\n\n===== ATUALIZAÇÃO DE DISCIPLINA =====\n")
    if len(listaDisciplinas) < 1:
        print('Não há disciplinas para atualizar.')
    else:
        for i, disciplina in enumerate(listaDisciplinas):
            print(
                f"{i + 1}. Código: {disciplina['Código']}, Nome: {disciplina['Nome']}")
        try:
            indice_edicao = int(
                input('Informe o número da disciplina que deseja editar: ')) - 1

            if 0 <= indice_edicao < len(listaDisciplinas):
                novo_nome = input('Insira o novo nome da disciplina: ')
                listaDisciplinas[indice_edicao]['Nome'] = novo_nome
                print(
                    f'A disciplina foi atualizada para "{novo_nome}" com sucesso.')
            else:
                print('Número de disciplina inválido.')
        except ValueError:
            print('Número inválido. Certifique-se de digitar um número válido.')


def atualizar_turma():
    print("\n\n===== ATUALIZAÇÃO DE TURMA =====\n")
    if len(listaTurmas) < 1:
        print('Não há turmas para atualizar.')
    else:
        for i, turma in enumerate(listaTurmas):
            print(
                f"{i + 1}. Código da Turma: {turma['Código']}, Código do Professor: {turma['Código do Professor']}, Código da Disciplina: {turma['Código da Disciplina']}")
        try:
            indice_edicao = int(
                input('Informe o número da turma que deseja editar: ')) - 1

            if 0 <= indice_edicao < len(listaTurmas):
                novo_codigo_professor = int(
                    input('Insira o novo código do professor da turma: '))
                novo_codigo_disciplina = int(
                    input('Insira o novo código da disciplina da turma: '))
                listaTurmas[indice_edicao]['Código do Professor'] = novo_codigo_professor
                listaTurmas[indice_edicao]['Código da Disciplina'] = novo_codigo_disciplina
                print(f'A turma foi atualizada com sucesso.')
            else:
                print('Número de turma inválido.')
        except ValueError:
            print('Número inválido. Certifique-se de digitar um número válido.')


def atualizar_matricula():
    print("\n\n===== ATUALIZAÇÃO DE MATRÍCULA =====\n")
    if len(listaMatriculas) < 1:
        print('Não há matrículas para atualizar.')
    else:
        for i, matricula in enumerate(listaMatriculas):
            print(
                f"{i + 1}. Código da Turma: {matricula['Código da Turma']}, Código do Estudante: {matricula['Código do Estudante']}")
        try:
            indice_edicao = int(
                input('Informe o número da matrícula que deseja editar: ')) - 1

            if 0 <= indice_edicao < len(listaMatriculas):
                novo_codigo_turma = int(
                    input('Insira o novo código da turma da matrícula: '))
                novo_codigo_estudante = int(
                    input('Insira o novo código do estudante da matrícula: '))
                listaMatriculas[indice_edicao]['Código da Turma'] = novo_codigo_turma
                listaMatriculas[indice_edicao]['Código do Estudante'] = novo_codigo_estudante
                print(f'A matrícula foi atualizada com sucesso.')
            else:
                print('Número de matrícula inválido.')
        except ValueError:
            print('Número inválido. Certifique-se de digitar um número válido.')









# EXCLUSÃO DE ENTIDADES

def excluir_estudante():
    print("\n\n===== EXCLUSÃO DE ESTUDANTE =====\n")
    if len(listaEstudantes) < 1:
        print('Não há estudantes para excluir.')
    else:
        for i, estudante in enumerate(listaEstudantes, start=1):
            print(
                f"{i}. Código: {estudante['Código']}, Nome: {estudante['Nome']}")
        try:
            indice_exclusao = int(
                input('Informe o número do estudante que deseja excluir: ')) - 1
            if 0 <= indice_exclusao < len(listaEstudantes):
                estudante_excluido = listaEstudantes.pop(indice_exclusao)
                print(
                    f'O estudante "{estudante_excluido["Nome"]}" foi excluído com sucesso.')
            else:
                print('Número de estudante inválido.')
        except ValueError:
            print('Número inválido. Certifique-se de digitar um número válido.')


def excluir_professor():
    print("\n\n===== EXCLUSÃO DE PROFESSOR =====\n")
    if len(listaProfessores) < 1:
        print('Não há professores para excluir.')
    else:
        for i, professor in enumerate(listaProfessores, start=1):
            print(
                f"{i}. Código: {professor['Código']}, Nome: {professor['Nome']}, CPF: {professor['CPF']}")
        try:
            indice_exclusao = int(
                input('Informe o número do professor que deseja excluir: ')) - 1
            if 0 <= indice_exclusao < len(listaProfessores):
                professor_excluido = listaProfessores.pop(indice_exclusao)
                print(
                    f'O professor "{professor_excluido["Nome"]}" foi excluído com sucesso.')
            else:
                print('Número de professor inválido.')
        except ValueError:
            print('Número inválido. Certifique-se de digitar um número válido.')


def excluir_disciplina():
    print("\n\n===== EXCLUSÃO DE DISCIPLINA =====\n")
    if len(listaDisciplinas) < 1:
        print('Não há disciplinas para excluir.')
    else:
        for i, disciplina in enumerate(listaDisciplinas, start=1):
            print(
                f"{i}. Código: {disciplina['Código']}, Nome: {disciplina['Nome']}")
        try:
            indice_exclusao = int(
                input('Informe o número da disciplina que deseja excluir: ')) - 1
            if 0 <= indice_exclusao < len(listaDisciplinas):
                disciplina_excluida = listaDisciplinas.pop(indice_exclusao)
                print(
                    f'A disciplina "{disciplina_excluida["Nome"]}" foi excluída com sucesso.')
            else:
                print('Número de disciplina inválido.')
        except ValueError:
            print('Número inválido. Certifique-se de digitar um número válido.')


def excluir_turma():
    print("\n\n===== EXCLUSÃO DE TURMA =====\n")
    if len(listaTurmas) < 1:
        print('Não há turmas para excluir.')
    else:
        for i, turma in enumerate(listaTurmas, start=1):
            print(
                f"{i}. Código da Turma: {turma['Código']}, Código do Professor: {turma['Código do Professor']}, Código da Disciplina: {turma['Código da Disciplina']}")
        try:
            indice_exclusao = int(
                input('Informe o número da turma que deseja excluir: ')) - 1
            if 0 <= indice_exclusao < len(listaTurmas):
                turma_excluida = listaTurmas.pop(indice_exclusao)
                print(f'A turma foi excluída com sucesso.')
            else:
                print('Número de turma inválido.')
        except ValueError:
            print('Número inválido. Certifique-se de digitar um número válido.')


def excluir_matricula():
    print("\n\n===== EXCLUSÃO DE MATRÍCULA =====\n")
    if len(listaMatriculas) < 1:
        print('Não há matrículas para excluir.')
    else:
        for i, matricula in enumerate(listaMatriculas, start=1):
            print(
                f"{i}. Código da Turma: {matricula['Código da Turma']}, Código do Estudante: {matricula['Código do Estudante']}")
        try:
            indice_exclusao = int(
                input('Informe o número da matrícula que deseja excluir: ')) - 1
            if 0 <= indice_exclusao < len(listaMatriculas):
                matricula_excluida = listaMatriculas.pop(indice_exclusao)
                print(f'A matrícula foi excluída com sucesso.')
            else:
                print('Número de matrícula inválido.')
        except ValueError:
            print('Número inválido. Certifique-se de digitar um número válido.')


operacoes = {
    1: {
        "entidade": "ESTUDANTES",
        1: incluir_estudante,
        2: listar_estudantes,
        3: atualizar_estudante,
        4: excluir_estudante
    },
    2: {
        "entidade": "PROFESSORES",
        1: incluir_professor,
        2: listar_professores,
        3: atualizar_professor,
        4: excluir_professor
    },
    3: {
        "entidade": "DISCIPLINA",
        1: incluir_disciplina,
        2: listar_disciplinas,
        3: atualizar_disciplina,
        4: excluir_disciplina
    },
    4: {
        "entidade": "TURMA",
        1: incluir_turma,
        2: listar_turmas,
        3: atualizar_turma,
        4: excluir_turma
    },
    5: {
        "entidade": "MATRICULA",
        1: incluir_matricula,
        2: listar_matriculas,
        3: atualizar_matricula,
        4: excluir_matricula
    }
}

while True:
    menu_principal()
    op = int(input('Informe a opção desejada: '))

    if op == 1 or op == 2 or op == 3 or op == 4 or op == 5:
        if op in operacoes:
            entidade = operacoes[op]["entidade"]
            print(f"\n\n***** {entidade} MENU DE OPERAÇÕES *****\n")
            print('(1) Incluir.')
            print('(2) Listar.')
            print('(3) Atualizar.')
            print('(4) Excluir.')
            print('(9) Voltar ao menu principal.\n')
            acao = int(input('Informe a ação desejada: '))
            if acao in operacoes[op]:
                operacoes[op][acao]()  # Chama a função correspondente
            elif op == 9:
                input("Pressione ENTER para continuar.")
            else:
                print("Voltando ao menu!")
        else:
            print("Opção de entidade incorreta!")
            input("Pressione ENTER para continuar.")
    elif op == 9:
        print("Finalizando aplicação...")
        break
    else:
        print("\nOpção incorreta!\n")
        input("Pressione ENTER para continuar.")
        continue
