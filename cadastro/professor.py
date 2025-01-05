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
    
    dados_da_escola.dados_escola["professores"].append(professor)
    print("professor cadastrado com sucesso")
