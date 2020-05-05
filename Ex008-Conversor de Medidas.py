medida=float(input('Uma distância em metros: '))
km=medida/1000
hm=medida/100
dam=medida/10
dm=medida*10
cm=medida*100
mm=medida*1000

print('A medida de {} corresponde a \n{:.3f}km \n{:.2f}hm \n{:.2f}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(medida,km,hm,dam,dm,cm,mm))
#a barra para pular linha é \n e não /n!
