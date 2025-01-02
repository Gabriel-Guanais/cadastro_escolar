from controle import resposta_usr
from aluno import cadastrar_aluno, lista_aluno

if resposta_usr == 1:
    cadastrar_aluno()
elif resposta_usr == 2:
    lista_aluno()
else:
    print("funcionou")




