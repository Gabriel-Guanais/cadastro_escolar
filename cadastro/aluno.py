from cadastro.save_in_json import salvar_no_json
import json
import uuid


alunos = []
        

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
        
        "nome" : nome,
        "matricula" : matricula,
        "data_nascimento" : data_nascimento,
        "sexo" : sexo,
        "endereço" : endereço,
        "telefone" : telefone,
        "email" : email 
    }
    
    salvar_no_json("dados_escolares.json", "alunos", aluno)
    
    
def lista_aluno():
    try:
        with open("dados_escolares.json", "r") as arquivo:
            alunos_exist = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        alunos_exist = []         
    
    nomes_lista = [list(aluno.values())[0]['nome'] for aluno in alunos_exist]
    print(f"nome dos alunos cadastrados: {nomes_lista}")
    


    
