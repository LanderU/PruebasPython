#!/usr/bin/python3

while True:
    try:
        mes = int(input("Numero del mes: "))
        if mes >= 1 and mes <= 12:
            break
        else:
            print("Recuerda que los meses van del 1 al 12...")
    except NameError:
        print("No valido...")
        print("Intentalo otra vez")

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 10 or mes == 12:
    print("El mes, %d tiene 31 dias" % mes)
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("El mes, %d tiene 30 dias" % mes)
elif mes == 2:
    print("El mes, %d tiene 28 dias" % mes)
