class nodo:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.siguiente = None
        self.anterior = None
        
def insertarNodo(self,nuevoNodo): 
    if self.cabecera:
        ultimoNodo = self.cabecera
    while ultimoNodo != None:
        ultimoNodo = ultimoNodo.siguiente
        ultimoNodo.seguiente = nuevoNodo
    else: 
        self.cabecera = nuevoNodo

def lista():
    def __init__ (self):
        self.cabecera = None
        
    
def eliminarNodo(self, key):
    actual = self.cabecera
    previo = None
    while actual and actual.dato != key:
        previo = actual
        actual = actual.siguiente
    if previo is None:
        self.cabecera = actual.siguiente
    else:
        previo.siguiente = actual.siguiente
        actual.siguiente = None

def buscarNodo(self, key):
    actual = self.cabecera
    while actual and actual.dato != key:
        actual = actual.siguiente
    return actual

def imprimirLista(self):
    actual = self.cabecera
    while actual != None:
        print(actual.dato, end="->")
        actual = actual.siguiente
    print("Null")

if __name__ == "__main__":
    lista = lista()
  


















    