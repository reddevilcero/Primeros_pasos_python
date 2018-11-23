import pickle, io

class Personaje:

    def __init__ (self, nombre, vida, ataque, defensa, alcance):

        try:

            self.nombre = nombre
            self.vida = int(vida)
            self.ataque = int(ataque)
            self.defensa = int(defensa)
            self.alcance = int(alcance)

        except:
            print('Los valores vida, ataque, defensa y alcance deben ser numeros.')


    def __str__ (self):

        return f'Personaje de tipo {self.nombre}\nVida ==> {self.vida}\nAtaque ==> {self.ataque}\nDefensa ==> {self.defensa}\nAlcance ==> {self.alcance}'   

class Gestor:

    personajes = []
    
    def __init__ (self ):

        self.cargar()

    def agregar(self, nuevo_personaje):

        for p in self.personajes:
            if p.nombre == nuevo_personaje.nombre:
                print(f'El personaje {nuevo_personaje.nombre} ya existe')
                return

        self.personajes.append(nuevo_personaje)     
        self.guardar()



    def mostrar(self):

        for personaje in self.personajes:
            print("\n",personaje)           

    def borrar(self, del_personaje):

        index = None

        for p in self.personajes:
            if p.nombre == del_personaje.nombre:
                index = self.personajes.index(p)
        
        if index != None:
            del(self.personajes[index])
            self.guardar()
            print(f'Personaje {del_personaje.nombre} borrado')
            return
        else:
            print('Personaje no encontrado')
            return  
            

        
    def cargar(self):

        fichero = open('personajes.pckl', 'ab+')
        fichero.seek(0)

        try:
            self.personajes = pickle.load(fichero)

        except:
            print("el fichero esta vacio")

        finally:
            fichero.close()
            print(f'Se han cargado {len(self.personajes)} personajes')


    def guardar(self):
        fichero = open('personajes.pckl', 'wb')
        pickle.dump(self.personajes, fichero)
        fichero.close()



arquero = Personaje('Arquero', 2, 4, 1, 8)
guerrero = Personaje('Guerrero', 2, 4.7, 2, 4)
caballero = Personaje('Caballero', 4, 2, 4, 2)

personajes = [arquero, guerrero, caballero]

gestor = Gestor()

gestor.borrar(arquero)

gestor.mostrar()
