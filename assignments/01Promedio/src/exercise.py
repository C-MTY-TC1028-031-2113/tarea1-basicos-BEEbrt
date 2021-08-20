print("Programa para calcular promedios de valores")
suma=0
contador=0
promedio=0
valor_r=int(input("Introduzca el numero de materias "))
for i in range(valor_r):
    valor_n= int(input("Ingresa tus calificaciones: "))
    suma=suma+valor_n
promedio=suma/valor_r
print("El promedio de las " + str(valor_r) +" materias es: " + str(promedio))
