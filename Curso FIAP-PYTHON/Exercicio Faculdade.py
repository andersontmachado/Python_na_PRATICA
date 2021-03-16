alunos=0
maior=0
nome_aluno_maior=''
for c in range(1,4):
    alunos = str(input(f'Digite o {c}º do aluno: ').upper())
    altura=float(input('Digite a altura do aluno: '))
    if altura > maior:
        nome_aluno_maior=alunos
        maior+=1

print(f'Altura maior é {altura} e o aluno é {alunos}')



