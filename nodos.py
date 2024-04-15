import os

os.system("cls")

class Nodo:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.siguiente = None
        

class Lista:
    def __init__(self):
        self.cabecera = None
    
    def insertarNodoCola(self):
        print('Ha elegido la opción 1: insertar una nueva persona')
        dni = input("Ingrese el numero de DNI de la persona: ")
        nombre= input("Ingrese el nombre de la persona: ")
        Apellido = input("Ingrese el apellido de la persona: ")
        nuevoNodo = Nodo(dni, nombre, Apellido)
        if self.cabecera:
            ultimoNodo = self.cabecera
            while ultimoNodo.siguiente != None:
                ultimoNodo = ultimoNodo.siguiente
            ultimoNodo.siguiente = nuevoNodo
        else: 
            self.cabecera = nuevoNodo
        self.imprimirLista()

    def insertarNodoCabecera(self):
        print('Ha elegido la opción 1: insertar una nueva persona')
        dni = input("Ingrese el numero de DNI de la persona: ")
        nombre= input("Ingrese el nombre de la persona: ")
        Apellido = input("Ingrese el apellido de la persona: ")
        nuevoNodo = Nodo(dni, nombre, Apellido)
        if self.cabecera is None:
            self.cabecera = nuevoNodo
            return
        nuevoNodo.siguiente = self.cabecera
        self.cabecera = nuevoNodo
        self.imprimirLista()

    def imprimirLista(self):
        actual = self.cabecera
        while actual != None:
            print(f"DNI:{actual.dni}, Nombre:{actual.nombre}, Apellido:{actual.apellido}",end=" -> ")
            actual = actual.siguiente
        print("Null")


        
    def eliminarNodo(self):
        dni = input("Ingrese el numero de DNI de la persona que desea eliminar: ")
        actual = self.cabecera
        previo = None
        while actual and actual.dni != dni:
            previo = actual
            actual = actual.siguiente
        if previo is None:
            self.cabecera = actual.siguiente
        elif actual:
            previo.siguiente = actual.siguiente
            actual.siguiente = None
        self.imprimirLista()

    def buscarNodo(self):
        dni = input("Ingrese el numero de DNI de la persona que desea buscar: ")
        actual = self.cabecera
        while actual and actual.dni != dni:
            actual = actual.siguiente
        return actual
    
    def contarNodos(self):
        contador = 0
        actual = self.cabecera
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador
        




if __name__ == "__main__":
    lista = Lista()

    print("---Bienvenido al Sistema de Alumno---")

    while True: 
        print("Menu:")
        print("opcion 1: Insertar nodo por cabecera ")
        print("opcion 2: Insertar nodo por cola ")
        print("opcion 3: Buscar por dni ")
        print("opcion 4: Eliminar una persona")
        print("opcion 5: Imprimir lista")
        print("opcion 6: Mostrar cantidad de alumnos")
        print("opcion 7: Salir")
        
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            lista.insertarNodoCabecera()
        elif opcion == "2":
            lista.insertarNodoCola()
        elif opcion == "3":
            resultado = lista.buscarNodo()
            if resultado:
                print(f"Persona encontrada: DNI:{resultado.dni}, Nombre:{resultado.nombre}, Apellido:{resultado.apellido}")
            else:
                print("persona no encontrads")
        elif opcion == "4":
            lista.eliminarNodo()
        elif opcion == "5":
            lista.imprimirLista()
        elif opcion == "6":
            print(f"Cantidad de alumnos: {lista.contarNodos()}")
        elif opcion == "7":
            print("Ejecucion finalizada")
            exit()
        else:
            print("opcion no valida")
        


















            