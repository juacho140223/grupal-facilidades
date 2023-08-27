# Universidad Central del Ecuador
# Carrera de Petroleos
# Materia: Facilidades de Producción
# Integrantes: Vanessa Chamorro, Ana Paula Carrasco, Dorian Erazo, Juan Salazar, Karen Zhangallimbay

#### Datos ####
# Grados API=15°
# Viscocidad del petróleo= 0.002 (lb/ft-s)
bfpd=75000
bwpd=2300
emul=30
va= 110 # Velocidad de asentamiento de las gotas de agua
###############
# Cálculo de los barriles de petróleo
bopd=bfpd-bwpd
# Cálculo del agua emulsionada
h2oe=bopd*emul/(100-emul)
# Cálculo del agua libre
h2ofr=bwpd-h2oe
# Cálculo de la emulsión
emul=bopd+h2oe
# Cálculo de la densidad relativa del petróleo
dro=141.5/(15+131.5)
# Cálculo de la densidad del petróleo
po=dro*62.4    # 62.4 densidad del agua en lb/ft^3
# Cálculo del diametro de la gota de agua
dgh2o=((va*0.002)/((62.4-po)*2.061131*10**5))**0.5
# Impresión de resultados
print(f'Agua emulsionada= {h2oe:0.3f}')
print(f'Emulsión= {emul:0.3f}')
print(f'Agua libre= {h2ofr:0.3f}')
print(f'Densidad del petróleo= {po:0.3f}')
print(f'El diámetro de la gota de agua es de: {dgh2o:0.3f} (um)')
