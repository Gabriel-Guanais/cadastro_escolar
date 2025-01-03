

ciano = "\033[96m"
reset = "\033[0m"
def menu():
    print(f'======================{ciano}IFMS{reset}=======================')
    print(f"| [{ciano}1{reset}] Cadastro Aluno                             |")
    print(f"| [{ciano}2{reset}] Cadastrar Professor                        |")
    print(f"| [{ciano}3{reset}] Cadastrar Disciplina                       |")
    print(f"| [{ciano}4{reset}] Cadastrar Turma                            |")
    print(f"| [{ciano}5{reset}] Matricular Aluno em Turma                  |")
    print(f"| [{ciano}6{reset}] Alocar Professor em diciplinas             |")
    print(f"| [{ciano}7{reset}] Alocar Diciplina em Turma                  |")
    print(f"| [{ciano}8{reset}] Filtrar Professores por Diciplina          |")
    print(f"| [{ciano}9{reset}] Listar Alunos Matriculado em Turmas        |")
    print(f"|[{ciano}10{reset}] Listar Professores alocados em disciplinas |")
    print(f"|[{ciano}11{reset}] Listar Diciplinas alocadas em turmas       |")
    print(f"| [{ciano}0{reset}]  Sair                                      |")
    print("=================================================================")

    try:
        escolha_usr = int(input(f"{ciano}Insira a Opção: {reset}"))
        return escolha_usr
    except ValueError:
        print("Número Invalido") 
        
resposta_usr = menu()