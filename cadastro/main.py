from controle import resposta_usr
from aluno import cadastrar_aluno
from professor import cadastrar_professor 
from diciplina import cadastrar_diciplina
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

if resposta_usr == 1:
    limpar_tela()
    cadastrar_aluno()
    
elif resposta_usr == 2:
    limpar_tela()
    cadastrar_professor()

elif resposta_usr == 3:
    limpar_tela()
    cadastrar_diciplina()
    
elif resposta_usr == 4:
    limpar_tela()
    ...
    
elif resposta_usr == 5:
    limpar_tela()
    ...
    
elif resposta_usr == 6:
    limpar_tela
    ...
    
    
else:
    print("funcionou")



