from lse_coes import Lista_SE

class Carro:
    """CLase que implementa el funcionamiento de un carro, que posee una placa, marca y modelo. Tener en cuenta lo siquiente
    - la placa tiene que tener el formato :"LLL NNN", donde L es letra y N es numero
    - los modelos validos son a partir del año 2000 unicamnete. Por defecto el año del modelo sera 2000
    - Un carro sera igual que otro si tienen la misma placa y marca
    """

    
    
    def __init__(self, placa, marca, modelo=2000):

            self.placa = placa
            self.marca = marca
            self.modelo = modelo
        
    @property
    def modelo(self):
         return self.__modelo

    @modelo.setter
    def modelo(self, año_modelo):
        if año_modelo > 2000:
              self.__modelo = año_modelo
        else:
            raise ValueError("No se pudo crear el carro!")
              

        
        
            

    def __eq__(self, otro_car):
        # validar que los dos carros sean de la misma clase
        return self.placa == otro_car.placa and self.marca == otro_car.marca

    def __str__(self):
        return f"{self.placa}/{self.marca}/{self.modelo}"
    

    
    




if __name__ == "__main__":
    # list_cad = Lista_SE()
    # list_cad.adicionar("Mesa")
    # list_cad.adicionar("Conejo")
    # list_cad.adicionar("Arroz")
    # list_cad.adicionar("Serpiente")
    # list_cad.recorrer()
    # print(f"Buscar: {list_cad.encontrar("Arroz")}")

    lst_cars = Lista_SE()
    try:
        car1 = Carro("QKJ 789", "Renault", 2001)
        car1.modelo = 1986
        lst_cars.adicionar(car1)
    except ValueError as e:
         print(e)


    carb = Carro("AWX 456", "Mazda", 2005)
    lst_cars.adicionar(carb)
    lst_cars.adicionar(Carro("RTY 123", "TOyota", 2018))
    lst_cars.recorrer()

    # placa = input("Placa a buscar:")
    # marca = input("Marca a buscar:")

    # car2 = Carro(placa, marca)
    # print(car1 == car2)
    # print(f"Buscar el carro 1: {lst_cars.encontrar(car2)}")    



