from save_in_json import salvar_no_json
import uuid


def cadastrar_turma():
    print(40*"=")
    print("BEM-VINDO A TELA DE CADASTRO DE TURMAS")
    print(40*"=")
    print("Preencha os espaços abaixo: \n")
    
    nome = input("digite o nome da turma: ")
    codigo = f"A{str(uuid.uuid4())[:5]}"
    professor = input("Digite o codigo do professor responsavel: ")
    diciplinas = input("Digite os codigos das diciplinas (separados por virgulas):").split(",")
    alunos = input("Digite as matriculas do alunos (separados por virgulas):").split(",")
    
    turma = {
        "nome": nome,
        "professor": professor,
        "codigo": codigo,
        "diciplinas": diciplinas,
        "alunos": alunos
    }
    
    salvar_no_json("dados_escolares.json", "turmas", turma)