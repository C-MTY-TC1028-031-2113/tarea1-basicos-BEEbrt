def peso_mes():
    inicial= 1
    final= 0
    mes= 12
pinical =float(input("Dime tu peso inicial: "))
pfinal =float(input("Dime tu peso final: "))
mesesito =int(input("Dime en cuantos meses: "))
resultado= (pinical - pfinal) / mesesito
print ("Lo que se debe baja por mes es: ",resultado)