"""class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

Nodo1 = Nodo(42)
print(Nodo1.dato)
print(Nodo1.siguiente)

Nodo2 = Nodo(67)
print(Nodo2.dato) 
print(Nodo2.siguiente)


Nodo3 = Nodo(10)
print(Nodo3.dato) 
print(Nodo3.siguiente)

Nodo1.siguiente = Nodo2
Nodo2.siguiente = Nodo3

actual = Nodo1
contador = 1

while actual is not None:
    print(f"Nodo {contador} Dato {actual.dato} Direccion {id(actual)}")
    actual = actual.siguiente
    contador += 1"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def show(self):
        print(f"Data = {self.data}")      
        print(f"Next = {self.next}") 


class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_first(self, data):
        new_node = Node(data)
        if (self.head == None):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def insert_last(self,data):
        new_node = Node(data)
        if (self.head == None):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def insert_at(self, data, position):
        if (position == 0):
            print("position = 0")
            self.insert_first(data)
        elif (position == self.size-1):
            print(f"position = {self.size-1}")
            self.insert_last(data)
        elif (position > self.size):
            print(f"position mayor que {self.size}")
            print("ERROR.... The data can´t be inserted")
        else:
            print("ok")
            previous = self.head
            k=0
            while k < position-1:
                previous = previous.next
                new_node = Node(data)
                new_node.next = previous.next
                previous.next = new_node
                k += 1 # Antes me saltaba error porque no le habia puesto este contador
            self.size += 1 


    def show_list(self):
        print(f"Head = {self.head} --- Tail = {self.tail} --- Size = {self.size}")
        print("Nodes: ")
        current = self.head
        while current is not None:
            print(f"data = {current.data} ---> next = {current.next}")
            current = current.next

new_list = Linked_list()
new_list.insert_first(43)
new_list.insert_last(10)
print(f"Tamaño de la lista: {new_list.size}")
new_list.show_list()
new_list.insert_at(2,2)
new_list.insert_at(4,7)