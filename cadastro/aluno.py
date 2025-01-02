import json
import uuid


alunos = []

#json esta me dando dor de cabeça...
def salvar_cadastro (nome_doc, dados):
    try:
        with open(nome_doc, "r") as arquivo:
            alunos_exist = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        alunos_exist = []

    alunos_exist.append(dados)

    with open(nome_doc, "w") as arquivo:
        json.dump(alunos_exist, arquivo, indent=4)
        

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
    
def lista_aluno():
    try:
        with open("logins.json", "r") as arquivo:
            alunos_exist = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        alunos_exist = []         
    
    nomes_lista = [list(aluno.values())[0]['nome'] for aluno in alunos_exist]
    print(f"nome dos alunos cadastrados: {nomes_lista}")
    


    
