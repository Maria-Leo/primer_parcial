

class Climas:
    def __init__(self):
        self.codigo = []
        self.ciudad = []
        self.tempMinima =[]
        self.tempMaxima = []
        self.zona = []
        self.estado = []

    def menu(self):
        opciones = """
                 ****Menu del Clima****
            
            1.-MOSTRAR CLIMAS DE CIUDADES
            2-.MOSTRAR PROMEDIO DE TEMPERATURAS MINIMAS 
            3.-MOSTRAR TEMPERATURA MAS BAJA 
            4.-MOSTRAR TEMPERATURA MAS ALTA 
            5.-SALIR
        
        """
        print(opciones)
        elegir = int(input("Elija una opcion del menu: \n"))
        if(elegir == 1):
            print(self.mostrar())
            self.volverMenu()
        elif(elegir == 2):
            print(self.promedioMin())
            self.volverMenu()
        elif (elegir == 3):
            pass
        elif (elegir == 4):
            print(self.promedioMax())
            self.volverMenu()
        elif (elegir == 5):
            print("Gracias por utilizar el sistema")
        else:
            print("Elija una opcion del menu!")
            self.menu()

    def volverMenu(self):
        eleccion= input("Desea volver al menu? s/n: \n")
        if (eleccion == "s" or eleccion == "S"):
            self.menu()

    def registrar(self):
        codigo = int(input("Agregue un codigo: \n"))
        ciudad = input("Agregar nueva ciudad: \n")
        minima = int(input("Tempertura minima: \n"))
        maxima = int(input("Temperatura maxima: \n"))
        zona = (input("agregue una zona"))
        print(self.guardar(codigo,ciudad,minima,maxima,zona))
        pass

    def guardar(self, codigo, ciudad, minima, maxima,zona):
        self.codigo.append(codigo)
        self.ciudad.append(ciudad)
        self.tempMinima.append(minima)
        self.tempMaxima.append(maxima)
        self.zona.append(zona)
        self.estado.append(1)
        return "Ciudad {} registrada exitosamente.!! ".format(ciudad)

    def mostrar(self):
        for i in range(len(self.ciudad)):
          self.detalle(i)
        return "**********************************"

    def detalle(self, posicion):
        print("Codigo de ciudad {} ".format(self.codigo[posicion]))
        print("Nombre de la ciudad: {} ".format(self.ciudad[posicion]))
        print("Temperatura Minima: {} ".format(self.tempMinima[posicion]))
        print("Temperatura Maxima: {} ".format(self.tempMaxima[posicion]))
        print("Zona: {} ".format(self.zona[posicion]))
        print("***********************************")


    def promedioMin(self,):
        print("***Temperaturas minimas***")
        for i in range(len(self.zona)):
            print(self.tempMinima[i], ("  "),self.zona[i])
        suma= 0
        for i in range(len(self.zona)):
            suma += self.tempMinima[i]
        return "*********"

    def promedioMax(self,):
        print("***TEmperaturas maximas***")
        for i in range(len(self.zona)):
            print(self.tempMaxima[i], ("  "),self.zona[i])
        suma= 0
        for i in range(len(self.zona)):
            suma += self.tempMaxima[i]
        pass



climas = Climas()
climas.guardar(1, "SANTA CRUZ", 15, 29, "Llano")
climas.guardar(2, "BENI", 17, 31,"Llano")
climas.guardar(3, "PANDO", 18, 30,"Llano")
climas.guardar(4, "LA PAZ", 1, 13,"Altiplano")
climas.guardar(5, "ORURO", 2, 15,"Altiplano")
climas.guardar(6, "POTOSI", 2, 14,"Altiplano")
climas.guardar(7, "CBBA", 5, 18, "Valle")
climas.guardar(8, "SUCRE", 9, 23, "Valle")
climas.guardar(9, "TARIJA", 10, 25, "Valle")
climas.menu()
