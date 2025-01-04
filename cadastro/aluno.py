from save_in_json import salvar_no_json
import json
import uuid


alunos = []
        

def cadastrar_aluno():
    
    print(30*"=")
    print("BEM-VINDO A TELA DE CADASTRO DO ALUNO")
    print(30*"=")
    print("Preencha os espaços abaixo: \n")

    
    nome = str(input("Digite o nome completo: "))
    matricula = f"A{str(uuid.uuid4())[:5]}"
    data_nascimento = input("Digite a data de nascimento: ") 
    sexo = input("Digite o Sexo: ")
    endereço = input("Digite o Endereço (Rua,numero):")
    telefone = input("Telefone:") 
    email = input("Email:") 
    
    aluno = {
        
        "nome" : nome,
        "matricula" : matricula,
        "data_nascimento" : data_nascimento,
        "sexo" : sexo,
        "endereço" : endereço,
        "telefone" : telefone,
        "email" : email 
    }
    
    salvar_no_json("dados_escolares.json", "alunos", aluno)
    
def matricular_aluno_turma():
    from save_in_json import salvar_no_json
    import json 
    
    print(20*"=")
    print("MATRICULAR ALUNO")
    print(20*"=")
    print("preencha os espaços abaixo: \n")
    
    
    try:
        with open("dados_escolares.json", "r") as arquivo:
            dados = json.load(arquivo) 
    except FileNotFoundError:
        print("nenhum dado encontrado")
        return
    
    if "turmas" not in dados or not dados["turmas"]:
        print("nenhuma turma cadastrada")
        return
    
    print("Turmas encontradas:")
    for turma in dados["turmas"]:
        print(f"Código: {turma['codigo']} | Nome: {turma['nome']}")
    
    codigo_turma = input("digite o coidigo da turma:")
    matricula_aluno = input("digite a matricula do aluno:")
    
    for turma in dados["turmas"]:
        if turma["codigo"] == codigo_turma:
            if matricula_aluno not in turma["alunos"]:
                turma["alunos"].append(matricula_aluno)
                salvar_no_json("dados_escolares.json", "turmas", turma)
                print("Aluno matriculado com sucesso!")
                return
            else:
                print("Aluno já está matriculado nesta turma.")
                return
    
    print("Turma não encontrada.")

    
    


    
