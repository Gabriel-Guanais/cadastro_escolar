from controle import resposta_usr
from aluno import cadastrar_aluno, matricular_aluno_turma
from professor import cadastrar_professor, alocar_professor_disciplina 
from diciplina import cadastrar_diciplina
from turma import cadastrar_turma
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
    cadastrar_turma()
    
elif resposta_usr == 5:
    limpar_tela()
    matricular_aluno_turma()
    
    
elif resposta_usr == 6:
    limpar_tela()
    alocar_professor_disciplina()

elif resposta_usr == 7:
    limpar_tela()
    ...
elif resposta_usr == 8:
    limpar_tela()
    ...
elif resposta_usr == 9:
    limpar_tela()
    ...
elif resposta_usr == 10:
    limpar_tela()
    ...
elif resposta_usr == 11:
    limpar_tela()
elif resposta_usr == 0:
    limpar_tela()
    print("---SAINDO---")
    ...     
else:
    ...



