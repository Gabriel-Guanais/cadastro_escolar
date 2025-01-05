import uuid
import dados_da_escola

def cadastrar_turma():
    print("=" * 40)
    print("BEM-VINDO À TELA DE CADASTRO DE TURMAS")
    print("=" * 40)
    print("Preencha os espaços abaixo:\n")
    
    nome = input("digite o nome da turma: ").strip()
    codigo = f"T{str(uuid.uuid4())[:5]}"  
    professor = input("digite o código do professor responsável: ").strip()
    
    diciplinas = input("digite os códigos das disciplinas (separados por vírgulas): ").split(",")
  
    
    alunos = input("digite as matrículas dos alunos: ").split(",") 

    turma = {
        "nome": nome,
        "codigo": codigo,
        "professor": professor,
        "disciplinas": diciplinas,
        "alunos": alunos
    }
    
    dados_da_escola.dados_escola["turmas"].append(turma)
    print(f"turma '{nome}' cadastrada com sucesso!")
