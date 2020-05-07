from datetime import date
atual= date.today().year
totmaior=0
tomenor=0
for pess in range(1,8):
    nasc=int(input('Em que ano a {}ª pessoa nasceu: '.format(pess)))
    idade=atual-nasc
    if idade >=21:
        totmaior=totmaior+1
    else:
        tomenor=tomenor+1
print('\033[31mAo todo tivemos {} pessoas maiores\033[m'.format(totmaior))
print('\033[32mAo todo tivemos {} pessoas menores\033[m'.format(tomenor))













