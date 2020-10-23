#Definición de la clase Ingreso
class Ingreso:
    #Método para inicializar la clase
    def __init__(self):
        self.ingresosList = []

    #Método para agregar el registro de un ingreso
    def agregarIngreso(self, tranId, monto):
        ingresoDict = {"id": tranId,"Tipo":'Ingreso', "Monto": monto} 
        self.ingresosList.append(ingresoDict)

    #Método para retornar la lista de ingresos
    def mostrarIngresos(self):
        return self.ingresosList


#Definición de la clase Egreso
class Egreso:
    #Método para inicializar la clase
    def __init__(self):
        self.egresosList = []

    #Método para agregar el registro de un egreso
    def agregarEgreso(self, tranId, monto):
        
        egresoDict = {"id": tranId,"Tipo":'Egreso', "Monto": monto} 
        self.egresosList.append(egresoDict)

    #Método para retornar la lista de egresos
    def mostrarEgresos(self):
        return self.egresosList


#Definición de la clase Finanzas
class Finanzas:
    #Método para inicializar la clase
    def __init__(self):
        self.transactionList = []
        self.ingresos = Ingreso()
        self.egresos = Egreso()
        self.saldo = 0
        self.idCounter = 0


    #Método para registrar un ingreso
    def registrarIngreso(self, monto):
        
        #Asignación de ID
        self.idCounter += 1
        transactionId = self.idCounter

        #Convertir monto a float
        monto = float(monto)

        #Construcción del diccionario con los datos del registro
        transactionDict = {"id": transactionId,"Tipo":'Ingreso', "Monto": monto}
        
        #Anexión del diccionario a la lista de transacciones e ingresos
        self.transactionList.append(transactionDict)
        self.ingresos.agregarIngreso(transactionId, monto)

        #Actualización del saldo total
        self.saldo += monto


    #Método para registrar un ingreso
    def registrarEgreso(self, monto):
        
        #Asignación de ID
        self.idCounter += 1
        transactionId = self.idCounter

        #Convertir monto a float
        monto = float(monto)

        #Construcción del diccionario con los datos del registro
        transactionDict = {"id": transactionId,"Tipo":'Egreso', "Monto": monto}
        
        #Anexión del diccionario a la lista de transacciones e ingresos
        self.transactionList.append(transactionDict)
        self.egresos.agregarEgreso(transactionId, monto)

        #Actualización del saldo total
        self.saldo -= monto

    
    #Método para obtener el reporte de ingresos
    def reporteIngresos(self):

        #Obtención del la lista con los registros
        reporte = self.ingresos.mostrarIngresos()

        #Bucle para imprimir los registros
        for diccionario in reporte:
            print(f'El registro con id {diccionario.get("id")} contiene un ingreso de $ {diccionario.get("Monto"):.2f}')


    #Método para obtener el reporte de ingresos
    def reporteEgresos(self):

        #Obtención del la lista con los registros
        reporte = self.egresos.mostrarEgresos()

        #Bucle para imprimir los registros
        for diccionario in reporte:
            print(f'El registro con id {diccionario.get("id")} contiene un egreso de $ {diccionario.get("Monto"):.2f}')


    #Método para obtener el reporte de todas las transacciones
    def reporteTransacciones(self):

        #Bucle para imprimir las transacciones
        for diccionario in self.transactionList:
            print(f'El registro con id {diccionario.get("id")} contiene un {diccionario.get("Tipo")} de $ {diccionario.get("Monto"):.2f}')
    

    #Método para obtener el saldo total
    def reporteSaldo(self):
        print(f'El saldo total es de $ {self.saldo:.2f}')