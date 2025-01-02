import json

def salvar_no_json(nome_arquivo, categoria, dado):
    try:
        with open(nome_arquivo, "r") as arquivo:
            dados_gerais = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        dados_gerais = { "alunos": [], "professores": [], "turmas": [], "disciplinas": [] }
    
    if categoria not in dados_gerais:
        dados_gerais[categoria] = []
    
    dados_gerais[categoria].append(dado)
    
    with open(nome_arquivo, "w") as arquivo:
        json.dump(dados_gerais, arquivo, indent=4)
