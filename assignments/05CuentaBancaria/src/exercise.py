salmesant=float(input("Dime tu saldo de mes anterior: "))
ing=float(input("Dime tus ingresos: "))
egr=float(input("Dime tus egresos: "))
numcheq=int(input("Dame el numero de cheques expedidos: ")) 
resultado= (salmesant + ing - egr + numcheq) * .75
print("El saldo final de cuenta en el mes es: ",resultado)