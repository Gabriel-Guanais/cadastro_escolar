from controle import resposta_usr
from aluno import cadastrar_aluno
from professor import cadastrar_professor 
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

if resposta_usr == 1:
    limpar_tela()
    cadastrar_aluno()
    
elif resposta_usr == 2:
    limpar_tela()
    cadastrar_professor()
    
else:
    print("funcionou")



