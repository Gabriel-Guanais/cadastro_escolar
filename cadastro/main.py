from controle import menu 
from aluno import cadastrar_aluno, matricular_aluno, listar_alunos_matriculados_e_turma
from professor import cadastrar_professor, alocar_professor_na_diciplina, listar_professores_alocados
from diciplina import cadastrar_diciplina, alocacao_diciplinas_turmas, listar_diciplinas_alocadas
from turma import cadastrar_turma
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        resposta_usr = menu()
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
            matricular_aluno()
    
        elif resposta_usr == 6:
            limpar_tela()
            alocar_professor_na_diciplina()

        elif resposta_usr == 7:
            limpar_tela()
            alocacao_diciplinas_turmas()
            
        elif resposta_usr == 8:
            limpar_tela()
            ...
        elif resposta_usr == 9:
            limpar_tela()
            listar_alunos_matriculados_e_turma()
            
        elif resposta_usr == 10:
            limpar_tela()
            listar_professores_alocados()
            
        elif resposta_usr == 11:
            limpar_tela()
            listar_diciplinas_alocadas()
            
        elif resposta_usr == 0:
           limpar_tela()
           print("---SAINDO---")  
           break 
        else:
            print("Opção Inválida")
 
if __name__ == "__main__":
    main()
         
        