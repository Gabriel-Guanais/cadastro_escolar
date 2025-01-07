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
    print("=== alocar diciplina na turmas ===")
    
    codigo_diciplina = input("digite o codigo da diciplina: ")
    codigo_turma = input("digite o codigo da turma: ")
    
    for disciplina in dados_da_escola.dados_escola["disciplinas"]:
        if disciplina["codigo"] == codigo_diciplina:
            disciplina["turmas"].append(codigo_turma)
            
            dados_da_escola.dados_escola["alocacoes_diciplina_turmas"].append({
                "codigo_diciplina": codigo_diciplina,
                "codigo_turma": codigo_turma
            })
            
            print(f"diciplina {disciplina['nome']} foi alocada na turma {codigo_turma}")
            return
        
    print("diciplina nao existe")

def listar_diciplinas_alocadas():
    print("=== Lista de Diciplinas Alocadas ===")
    
    if not dados_da_escola.dados_escola["alocacoes_diciplina_turmas"]:
        print("Nada encontrado.")
        return
    
    for alocacao in dados_da_escola.dados_escola["alocacoes_diciplina_turmas"]:
        disciplina = next((d for d in dados_da_escola.dados_escola["disciplinas"] if d["codigo"] == alocacao["codigo_diciplina"]), None)
        turma = next((t for t in dados_da_escola.dados_escola["turmas"] if t["codigo"] == alocacao["codigo_turma"]), None)
        
        if disciplina and turma:
            print(f"diciplina {disciplina['nome']} está alocada na turma {turma['nome']}.")
        else:
            print("alocação inválida encontrada.")