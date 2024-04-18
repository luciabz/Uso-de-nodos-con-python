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
        if self.cabecera: #comprueba si hay nodos en la cola
            ultimoNodo = self.cabecera  # si hay nodos, se crea una variable que va a ser el ultimo nodo
            while ultimoNodo.siguiente != None: # mientras el siguiente nodo no sea nulo, se va a ir al siguiente nodo
                ultimoNodo = ultimoNodo.siguiente # en cada iteracion del bucle, la variable ultimoNodo se actualizara con el siguiente nodo en la cola
            ultimoNodo.siguiente = nuevoNodo # una vez q encuentra el ultimo nodo de la cola, se le asigna el nuevo nodo
        else: # si no hay nodos en la cola, se crea el primer nodo
            self.cabecera = nuevoNodo # se asigna el nuevo nodo a la cabecera
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

    def imprimirLista(self): # se crea un metodo para imprimir la lista
        print("Lista de personas: ")
        actual = self.cabecera # se crea una variable que va a ser el nodo actual
        while actual != None: # mientras el nodo actual no sea nulo, se va a imprimir el nodo actual
            print(f"DNI:{actual.dni}, Nombre:{actual.nombre}, Apellido:{actual.apellido}",end=" -> ") # se imprime el nodo actual
            actual = actual.siguiente # se actualiza el nodo actual con el siguiente nodo
        print("Null") # se imprime Null al final de la lista


        
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
    
    def contarNodos(self): # se crea un contador para contar la cantidad de nodos
        contador = 0 # se inicializa el contador en 0
        actual = self.cabecera # se crea una variable que apunte al primer nodo
        while actual: # mientras la variable actual sea diferente de None
            contador += 1 # se incrementa el contador
            actual = actual.siguiente # se avanza al siguiente nodo
        return contador # se retorna el contador
        




if __name__ == "__main__":
    lista = Lista()

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
        


















            