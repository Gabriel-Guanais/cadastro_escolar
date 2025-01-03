import uuid
from save_in_json import salvar_no_json

professores = []

def cadastrar_professor():
    print(30*"=")
    print("BEM-VINDO A TELA DE CADASTRO DO PROFESSOR")
    print(30*"=")
    print("Preencha os espaços abaixo: \n")
    
    nome = input("Digite seu nome completo: ")
    codigo = f"A{str(uuid.uuid4())[:5]}"
    data_nascimento = int(input("Digite a data de nascimento:"))
    sexo = input("Digite o sexo: ")
    endereço = input("Digite o seu enderço (rua, numero): ")
    telefone = input("Telefone:") 
    email = input("Email:")
    diciplina = input("Digite sua diciplina: ")
    
    professor = {
        
        "nome" : nome,
        "codigo" : codigo,
        "data_nascimento" : data_nascimento,
        "sexo" : sexo,
        "endereço" : endereço,
        "telefone" : telefone,
        "email" : email,
        "diciplina" : diciplina
    }
    
    salvar_no_json("dados_escolares.json", "professores", professor)
