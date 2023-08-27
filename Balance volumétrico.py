# Universidad Central del Ecuador
# Carrera de Petroleos
# Materia: Facilidades de Producción
# Integrantes: Vanessa Chamorro, Ana Paula Carrasco, Dorian Erazo, Juan Salazar, Karen Zhangallimbay

#### Datos ####
bfpd=20000
bwpd=7500
emul=25
ar=1000
efi=95
################
# Cálculo de los barriles de petróleo
bopd=bfpd-bwpd
#Agua emulsionada
aguaemul=bopd*emul/(100-emul)
# Cálculo del agua libre
agualib=bwpd-aguaemul
# Cálculo de la emulsión
emul1=bopd+aguaemul
# Cálculo de la pérdida de agua libre
pagualib=agualib*(100-efi)/100
# Cálculo del agua libre de la eficiencia del equipo
agualib1=agualib-pagualib
total=bopd+aguaemul+agualib
print(f'############ INLET ###########')
print(f'BOPD= {bopd:0.1f}')
print(f'Agua emulsionada= {aguaemul:0.4f}')
print(f'Emulsión= {emul1:0.4f}')
print(f'Agua libre= {agualib:0.4f}')
print(f'BFPD= {total:0.1f}')
#Iteración 1 
# Cálculo de la emulsión
emul1=bopd+aguaemul+pagualib
#Suma
total1=emul1+agualib1
print(f'########### Iteración 1 ###########')
print(f'BOPD= {bopd:0.4f}')
print(f'Agua emulsionada= {aguaemul:0.3f}')
print(f'Pérdida de agua libre= {pagualib:0.3f}')
print(f'Emulsión= {emul1:0.3f}')
print(f'Agua libre= {agualib1:0.3f}')
print(f'BFPD= {total1:0.1f}')
#Iteración 2 
# Cálculo del Aceite residual
ar2=agualib1*ar/(1000000-ar)
# Cálculo del petróleo resultante
bopd2=bopd-ar2
# Cálculo de la emulsión
emul2=bopd2+aguaemul+pagualib
# Cálculo del agua libre
agualib2=agualib1
#Suma
total2=emul2+agualib2+ar2
print(f'########### Iteración 2 ###########')
print(f'BOPD= {bopd2:0.1f}')
print(f'Agua emulsionada= {aguaemul:0.3f}')
print(f'Pérdida de agua libre= {pagualib:0.3f}')
print(f'Emulsión= {emul2:0.3f}')
print(f'Agua libre= {agualib2:0.3f}')
print(f'Aceite residual= {ar2:0.3f}')
print(f'BFPD= {total2:0.1f}')
#Iteración 3
# Cálculo del agua emulsionada 
aguaemul2=bopd2*emul/(100-emul)
#Variación de agua emulsionada
vaguaemul2=aguaemul-aguaemul2
# Cálculo de la emulsión
emul3=aguaemul2+bopd2+pagualib
# Cálculo del agua libre
agualib3=vaguaemul2+agualib2
#Suma
total3=emul3+agualib3+ar2
print(f'########### Iteración 3 ###########')
print(f'Agua emulsionada= {aguaemul2:0.3f}')
print(f'BOPD= {bopd2:0.1f}')
print(f'Pérdida de agua libre= {pagualib:0.3f}')
print(f'Emulsión= {emul3:0.3f}')
print(f'Agua libre= {agualib3:0.3f}')
print(f'Aceite residual= {ar2:0.3f}')
print(f'BFPD= {total3:0.1f}')
#Iteración 4
# Cálculo del Aceite residual
ar3=agualib3*ar/(1000000-ar)
#Variación de agua residual
var=ar3-ar2
# Cálculo del petróleo resultante
bopd3=bopd2-var
# Cálculo de la emulsión
emul4=bopd3+aguaemul2+pagualib
# Cálculo del agua libre
agualib4=agualib3
#Suma
total4=emul4+agualib4+ar3
print(f'########### Iteración 4 ###########')
print(f'BOPD= {bopd3:0.1f}')
print(f'Agua emulsionada= {aguaemul2:0.3f}')
print(f'Pérdida de agua libre= {agualib:0.3f}')
print(f'Emulsión= {emul4:0.3f}')
print(f'Agua libre= {agualib4:0.3f}')
print(f'Aceite residual= {ar3:0.3f}')
print(f'BFPD= {total4:0.1f}')
#Datos finales
# Cálculo del agua emulsionada
aguaemul3=bopd3*emul/(100-emul)
#Variación de agua emulsionada
vaguaemul=aguaemul2-aguaemul3
print(f'########### Iteración 5 ###########')
print(f'Agua emulsionada= {aguaemul3:0.3f}')
print(f'BOPD= {bopd3:0.3f}')
print(f'Agua libre= {agualib4:0.3f}')
print(f'Variación de agua emulsionada= {vaguaemul:0.4f}')