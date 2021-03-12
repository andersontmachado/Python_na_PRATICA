alunos=0
altura=0
maior=0
cont=0
for a in range(1,5):
    alunos = str(input(f'Digite o {a}º do aluno: ').upper())
    altura=str(input('Digite a altura do aluno: '))
    if altura in alunos:
        altura=maior
        maior=altura
    print(f'O aluno mais alto é o que tem {maior},chama-se {alunos}')









