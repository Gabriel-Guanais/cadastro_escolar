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
    print("aqui tem as turmas q vc pode escolher:")

    for turma in dados_escola["turmas"]:
        print(f"  - {turma['nome']} (cod: {turma['codigo']})")

    matricula = input("\ndigita  a matricula do aluno: ")
    codigo_turma = input("digite o codigo da turma: ")

    aluno = None
    for a in dados_escola["alunos"]:
        if a["matricula"] == matricula:
            aluno = a
            break

    if not aluno:
        print("hmm... nao achei esse aluno, confere a matricula .")
        return

    turma = None
    for t in dados_escola["turmas"]:
        if t["codigo"] == codigo_turma:
            turma = t
            break

    if not turma:
        print("essa turma nao existe, tenta outro cod.")
        return

    if matricula in turma["alunos"]:
        print(f"o aluno {aluno['nome']} já tá na turma {turma['nome']}")
    else:
        turma["alunos"].append(matricula)
        dados_escola["alunos_matriculados"].append({"matricula": matricula, "codigo_turma": codigo_turma})
        print(f" o aluno {aluno['nome']} foi colocado na turma {turma['nome']}.")

def listar_alunos_matriculados_e_turma():
    
    print("=== alunos matriculados e turmas ===")
    for m in dados_escola["alunos_matriculados"]:
        aluno = next((a for a in dados_escola["alunos"] if a["matricula"] == m["matricula"]), None)
        turma = next((t for t in dados_escola["turmas"] if t["codigo"] == m["codigo_turma"]), None)

        if aluno and turma:
            print(f"aluno: {aluno['nome']} - turma: {turma['nome']}")
        else:
            print(f"matricula {m['matricula']} não encontrada")