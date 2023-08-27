# Universidad Central del Ecuador
# Carrera de Petroleos
# Materia: Facilidades de Producción
# Integrantes: Vanessa Chamorro, Ana Paula Carrasco, Dorian Erazo, Juan Salazar, Karen Zhangallimbay

# Ingresar los valores de las variables
a=float(input('Ingrese el valor de área en acres: ')) 
b=float(input('Ingrese el valor de presión en bares: ')) 
c=float(input('Ingrese el valor de longitud en metros: ')) 
# Calculo de las variables
a=a*43560  
b=b*14.5038
c=c*3.28084
# Impresión de los resultados
print(f'El área es: {a:0.3f} ft^2') 
print(f'La presión es: {b:0.3f} psi') 
print(f'La longitud es: {c:0.3f} ft')
