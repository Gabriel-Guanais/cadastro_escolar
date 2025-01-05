
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
    
    diciplina = {
        "nome" : nome,
        "codigo" : codigo,
        "carga_horaria" : carga_horaria,
        "professor" : professor
    }
    
    