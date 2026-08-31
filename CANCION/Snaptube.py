class Snaptube:
    def __init__(self, titulo, artista, año, genero):
        self.titulo = titulo
        self.artista = artista
        self.año = año
        self.genero = genero
        self.siguiente = None

class Linked_list:
    def __init__(self):
        self.head = None

    def insert(self, titulo, artista, año, genero): # En el menu hay que hacer que lo puedan insertar por cada atributo
        new_song = Snaptube(titulo, artista, año, genero)

        if self.head is None:
            self.head = new_song
        else:
            actual = self.head

            while actual.siguiente is not None:
                actual = actual.siguiente

            actual.siguiente = new_song

    #def buscar(self, titulo):

    def eliminar(self):

        titulo = input("Ingrese el nombre de la cancion que desea eliminar: ")
        actual = self.head
        anterior = None

        while actual is not None:
            if actual.titulo.lower() == titulo.lower():
                if anterior is None:
                    self.head = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                print(f"La cancion {actual.titulo} fue eliminada.")
                return
            anterior = actual
            actual = actual.siguiente
        print("Cancion no encontrada.")

    def show_list(self):
        current = self.head
        while current is not None:
            print(f"Titulo: {current.data[0]}\n Artista: {current.data[1]}\n Año: {current.data[2]}\n Genero: {current.data[3]}")
    
list = Linked_list()

while True:
    print("SPOTIFY")
    print("1. Insertar cancion")
    print("2. Buscar cancion")
    print("3. Mostrar canciones")
    print("4. Eliminar canciones")
    print("5. Salir")


    option = input("Seleccione una opcion: ")

    if option == "1":
        print("INSERTAR CANCION:")
        titulo = input("Titulo: ")
        artista = input("Artista: ")
        año = input("Año: ")
        genero = input("Genero: ")

        list.insert(
            titulo,
            artista,
            año,
            genero
        )
    elif option == "2":
        print(input("Buscar cancion: "))
        list.buscar()
    elif option == "3":
        print("Mostrar canciones: ")
    elif option == "4":
        print("Eliminar Canciones")
        list.eliminar()

        list.show_list()
    elif option == "5":
        print("Saliendo del sistema...")
        break
    else:
        print("Opcion no valida")
        break
