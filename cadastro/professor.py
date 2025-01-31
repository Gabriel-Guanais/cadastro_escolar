import uuid
import dados_da_escola


def cadastrar_professor():
    print(40*"=")
    print("BEM-VINDO A TELA DE CADASTRO DO PROFESSOR")
    print(40*"=")
    print("Preencha os espaços abaixo: \n")
    
    nome = input("Digite seu nome completo: ")
    codigo = f"A{str(uuid.uuid4())[:5]}"
    data_nascimento = input("Digite a data de nascimento:")
    sexo = input("Digite o sexo: ")
    endereço = input("Digite o seu enderço (rua, numero): ")
    telefone = input("Telefone:") 
    email = input("Email:")
    disciplina = input("Digite sua diciplina: ")
    
    professor = {
        
        "nome" : nome,
        "codigo" : codigo,
        "data_nascimento" : data_nascimento,
        "sexo" : sexo,
        "endereço" : endereço,
        "telefone" : telefone,
        "email" : email,
        "disciplina" : disciplina,
        "diciplinas" : [] 
    }
    
    dados_da_escola.dados_escola["professores"].append(professor)
    print("professor cadastrado com sucesso")

def alocar_professor_na_diciplina():
    print("=== alocar professor na diciplina ===")
    
    codigo_diciplina = input("digite o codigo da diciplina: ")
    professor_alocad = input("digite o código do professor candidato: ")

    for professor in dados_da_escola.dados_escola["professores"]:
        if professor["codigo"] == professor_alocad:
            professor["diciplinas"].append(codigo_diciplina)
            
            dados_da_escola.dados_escola["alocacoes_professor_diciplina"].append({
                "codigo_professor": professor_alocad,
                "codigo_diciplina": codigo_diciplina
            })
            
            print(f"professor {professor['nome']} foi alocado na diciplina {codigo_diciplina}")
            return
    
    print("professor nao existe")

def listar_professores_alocados():
    print("=== Lista de Professores Alocados ===")

    if not dados_da_escola.dados_escola["alocacoes_professor_diciplina"]:
        print("Nada encontrado.")
        return

    for alocacao in dados_da_escola.dados_escola["alocacoes_professor_diciplina"]:
        professor = next((p for p in dados_da_escola.dados_escola["professores"] if p["codigo"] == alocacao["codigo_professor"]), None)
        disciplina = next((d for d in dados_da_escola.dados_escola["disciplinas"] if d["codigo"] == alocacao["codigo_diciplina"]), None)
        
        if professor and disciplina:
            print(f"professor {professor['nome']} está alocado na disciplina {disciplina['nome']}.")
        else:
            print("alocação inválida encontrada.")