import json
import uuid


alunos = []

#json esta me dando dor de cabeça...
def salvar_cadastro (nome_doc, dados):
    with open(nome_doc, "r") as arquivo:
        json.dump(dados,  arquivo, indent=4)

def cadastrar_aluno():
    
    print(30*"=")
    print("BEM-VINDO A TELA DE CADASTRO")
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
        
        matricula:{
            "nome" : nome,
            "matricula" : matricula,
            "data_nascimento" : data_nascimento,
            "sexo" : sexo,
            "endereço" : endereço,
            "telefone" : telefone,
            "email" : email 
        }

    }
    
    
    salvar_cadastro("logins.json", aluno)
    print(f"Cadastro Realizado...salve seu codigo de matricula para fazer login")
    

    
