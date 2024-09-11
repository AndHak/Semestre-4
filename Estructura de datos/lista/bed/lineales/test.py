from lse import Lista_SE

class Carro:
    """
     _summary_
     Clase que implementa el funcionamiento de un carro
     - que posee una placa, marca y modelo. Tener en cuenta lo siguiente
     la placa tiene que tener el formato: "LLL NNN", donde L es letra y N es numero.
     - Los modelos válidos son a partir del año 200, únicamente por defecto el
     año será 2000.
    """

    def __init__(self, placa, marca, modelo=2000):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo

    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, year_model):
        if year_model >= 2000:
            self.__modelo = year_model
        else:
            raise Exception("No se puede agregar el carro")


    def __str__(self):
        return f"Placa: {self.placa}\nMarca: {self.marca}\nModelo: {self.modelo}\n"
    
    def __eq__(self, otro_car):
        return (self.placa == otro_car.placa and self.marca == otro_car.marca)
    

if __name__ == "__main__":
    lst_cars = Lista_SE()
    try:
        car1 = Carro("QKJ 789", "Renault", 1999)
        lst_cars.adicionar(car1)
        car1.modelo = 1999
        car2 = Carro("AWX 456", "Mazda", 2005)
        lst_cars.adicionar(car2)
        car3 = Carro("RTY 159", "Toyota", 2018)
        lst_cars.adicionar(car3)
    except Exception as e:
        print(e)

    lst_cars.recorrer()
