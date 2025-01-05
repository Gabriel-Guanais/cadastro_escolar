import dados_da_escola
import uuid
  

def cadastrar_aluno():
    
    print(30*"=")
    print("BEM-VINDO A TELA DE CADASTRO DO ALUNO")
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
    
    print(dados_da_escola.dados_escola)
    dados_da_escola.dados_escola["alunos"].append(aluno)
    print(f"\naluno {nome} cadastrado com sucesso!")
    print(dados_da_escola.dados_escola)
    
def matricular_aluno_turma():
     
    print(20*"=")
    print("MATRICULAR ALUNO")
    print(20*"=")
    print("preencha os espaços abaixo: \n")
    
   