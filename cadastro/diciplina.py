from save_in_json import salvar_no_json
import uuid

def cadastrar_diciplina():
    
    print(40*"=")
    print("BEM-VINDO A TELA DE CADASTRO DA DICIPLINA")
    print(40*"=")
    print("Preencha os espaços abaixo: \n")
    
    nome = input("Digite seu nome da diciplina: ")
    codigo = f"A{str(uuid.uuid4())[:5]}"   
    carga_horaria = input("Digite a carga horaria: ")
    professor = input("Digite o professor: ")
    
    diciplina = {
        "nome" : nome,
        "codigo" : codigo,
        "carga_horaria" : carga_horaria,
        "professor" : professor
    }
    
    salvar_no_json("dados_escolares.json", "diciplinas", diciplina)
    