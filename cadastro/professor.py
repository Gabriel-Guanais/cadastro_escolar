import uuid
from save_in_json import salvar_no_json
import json



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
    
    salvar_no_json("dados_escolares.json", "professores", professor)

def alocar_professor_disciplina():
    try:
        with open("dados_escolares.json", "r") as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print("Nenhum dado encontrado.")
        return

    professores = dados.get("professores", [])
    disciplinas = dados.get("disciplinas", [])

    if not professores:
        print("Nenhum professor cadastrado.")
        return

    if not disciplinas:
        print("Nenhuma disciplina cadastrada.")
        return

    print("Professores disponíveis:")
    for i, professor in enumerate(professores):
        print(f"{i + 1}. {professor['nome']}")

    print("\nDisciplinas disponíveis:")
    for i, disciplina in enumerate(disciplinas):
        print(f"{i + 1}. {disciplina['nome']}")

    try:
        professor_index = int(input("\nSelecione o número do professor: ")) - 1
        disciplina_index = int(input("Selecione o número da disciplina: ")) - 1

        professor = professores[professor_index]
        disciplina = disciplinas[disciplina_index]

        alocacao = {
            "professor": professor['nome'],
            "disciplina": disciplina['nome']
        }

        salvar_no_json("dados_escolares.json", "alocacoes", alocacao)
        print(f"Professor {professor['nome']} alocado à disciplina {disciplina['nome']} com sucesso.")

    except (IndexError, ValueError):
        print("Seleção inválida. Tente novamente.")