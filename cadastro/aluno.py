from dados_da_escola import dados_escola
import uuid
  

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
    
    print(dados_escola)
    dados_escola["alunos"].append(aluno)
    print(f"\naluno {nome} cadastrado com sucesso!")
    print(dados_escola)
    
def matricular_aluno():
    print("=== sistema de matriculas ===")
    print("escolha uma das turmas abaixo:")

    for turma in dados_escola["turmas"]:
        print(f"{turma['nome']} (codigo: {turma['codigo']})")

    matricula = input("\ndigite a matricula do aluno: ")
    codigo_turma = input("digite o codigo da turma: ")

    aluno = next((a for a in dados_escola["alunos"] if a["matricula"] == matricula), None)
    if not aluno:
        print("aluno nao encontrado, verifique a matricula")
        return

    turma = next((t for t in dados_escola["turmas"] if t["codigo"] == codigo_turma), None)
    if not turma:
        print("turma nao encontrada verifique o codigo")
        return

    if aluno["matricula"] in [a["matricula"] for a in turma["alunos"]]:
        print(f"o aluno {aluno['nome']} ja esta matriculado na turma {turma['nome']}.")
    else:
        turma["alunos"].append(aluno)
        dados_escola["alunos_matriculados"].append({"matricula": matricula, "codigo_turma": codigo_turma})
        aluno["turma"] = codigo_turma
        print(f"aluno {aluno['nome']} matriculado na turma {turma['nome']}!")

def listar_alunos_matriculados_e_turma():
    
    print("=== alunos matriculados e turmas ===")

    for aluno in dados_escola["alunos"]:
        print(f"Matrícula: {aluno['matricula']}, Nome: {aluno['nome']}, Turma: {aluno['turma']},")