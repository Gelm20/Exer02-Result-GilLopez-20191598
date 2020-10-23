from finanzas import Ingreso, Egreso, Finanzas

print("Inicio Programa de control de finanzas: \n")

finanzasObj = Finanzas()


def showSaldo():
    finanzasObj.reporteSaldo()


def addIngreso():
    print('Ha seleccionado agregar un ingreso')
    monto = input('Indique el monto del ingreso: ')

    finanzasObj.registrarIngreso(monto)
    showSaldo()


def addEgreso():
    print('Ha seleccionado agregar un egreso')
    monto = input('Indique el monto del egreso: ')

    finanzasObj.registrarEgreso(monto)
    showSaldo()


def showIngresos():
    print('Ha seleccionado mostrar registro de ingresos')

    finanzasObj.reporteIngresos()


def showEgresos():
    print('Ha seleccionado mostrar registro de egresos')

    finanzasObj.reporteEgresos()


def showTransacciones():
    print('Ha seleccionado mostrar todos los registros')

    finanzasObj.reporteTransacciones()

while True:
    print("\n Menu: \n")
    print("(0) Salir")
    print("(1) Mostrar saldo")
    print("(2) Mostrar registros de ingresos")
    print("(3) Mostrar registros de egresos")
    print("(4) Mostrar todos los registros")
    print("(5) Agregar ingreso")
    print("(6) Agregar egreso \n")
    option = int(input("Ingrese el número de la acción que desea realizar: "))
    print("\n")

    if option == 0:
        print("Se ha finalizado el programa \n")
        break
    elif option == 1:
        showSaldo()
    elif option == 2:
        showIngresos()
    elif option == 3:
        showEgresos()
    elif option == 4:
        showTransacciones()
    elif option == 5:
        addIngreso()
    elif option == 6:
        addEgreso()