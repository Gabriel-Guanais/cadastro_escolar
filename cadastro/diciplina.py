import dados_da_escola
import uuid

def cadastrar_diciplina():
    
    print(40*"=")
    print("BEM-VINDO A TELA DE CADASTRO DA DICIPLINA")
    print(40*"=")
    print("Preencha os espaços abaixo: \n")
    
    nome = input("Digite o nome da diciplina: ")
    codigo = f"A{str(uuid.uuid4())[:5]}"   
    carga_horaria = input("Digite a carga horaria: ")
    professor = input("Digite o codigo do professor: ")
    
    disciplina = {
        "nome" : nome,
        "codigo" : codigo,
        "carga_horaria" : carga_horaria,
        "professor" : professor
    }
    
    dados_da_escola.dados_escola["disciplinas"].append(disciplina)
    print(f"diciplina '{nome}' criada com sucesso!")
    
def alocacao_diciplinas_turmas():
    ...