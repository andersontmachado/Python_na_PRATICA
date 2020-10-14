tabela=('Atlético - MG','Internacional','São Paulo','Palmeiras','Vasco','Flamengo',
'Fluminense','Sport','Santos','Fortaleza','Athetico - PR','Ceará','Atlético - GO',
'Corinthians','Grêmio','Bahia','Coritiba','Bragantino','Botafogo','Goiás')
print('Os cinco primeiro do Brasileirão são',tabela[1:6])
print('Os últimos quatro colocados são',tabela[-4:])
print('Times em ordem alfabética',sorted(tabela))
print(f'O Santos está na {tabela.index("Santos")+1}ª posição.')
'''o INDEX ele procura a posição que voce quer,daí coloca entre parenteses e acrescenta duas aspas
o time que vc escolheu +1 um,pq do mais1,pq ele começa a contagem com zero,pro normal sera
a posição 8,mais na verdade esta em nono.'''
print(list(tabela))
##coloquei a lista aqui pra tentar inumerar do 1 ao 20,mais sem sucesso,um debaixo do outro,


####Esse exercicío até a ordem alfabetica acertei sozinho,sem olhar,o Index não ia lembrar




