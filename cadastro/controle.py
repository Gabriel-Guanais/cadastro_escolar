

ciano = "\033[96m"
reset = "\033[0m"
def menu():
    print(f'=============={ciano}IFMS{reset}===============')
    print(f"| [{ciano}1{reset}] Cadastro Aluno             |")
    print(f"| [{ciano}2{reset}] Listar Aluno               |")
    print(f"| [{ciano}3{reset}] Cadastrar Professor        |")
    print(f"| [{ciano}4{reset}] Listar Professores         |")
    print(f"| [{ciano}5{reset}] Cadastrar Disciplina       |")
    print(f"| [{ciano}6{reset}] Listar Disciplinas         |")
    print(f"| [{ciano}7{reset}] Cadastrar Turma            |")
    print(f"| [{ciano}8{reset}] Listar Turma               |")
    print(f"| [{ciano}9{reset}] Matricular Aluno em Turma  |")
    print(f"|[{ciano}10{reset}] Alocar Diciplina em Turma  |")
    print(f"| [0] Sair                                     |")
    print("================================================")

    try:
        escolha_usr = int(input(f"{ciano}Insira a Opção: {reset}"))
        return escolha_usr
    except ValueError:
        print("Número Invalido") 
        
resposta_usr = menu()