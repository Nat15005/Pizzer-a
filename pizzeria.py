class Masa:
    def validarValor(self, valor, tipo):                #valida que los valores pertenezacan al tipo correcto de datos
        if valor in self.valores_permitidos.keys() and tipo in self.tipos.keys():
            return valor, tipo
        raise Exception("Masa incorrecta")

    def calcularPrecioMasa(self):                      #Calcula el precio de la masa
        return self.valores_permitidos[self.valor] + self.tipos[self.tipo]

    def __init__(self, valor, tipo):
        self.valores_permitidos = {                     #Se establecen los precios de la masa
            "p": 4000,
            "m": 6000,
            "l": 8000
        }
        self.tipos = {
            "d": 1000,
            "m": 2000,
            "g": 3000
        }
        self.valor, self.tipo = self.validarValor(valor, tipo)


class Servicio:

    def validarServicio(self, ad):                       #valida que los valores pertenezacan al tipo correcto de datos
        if ad in self.adiciones.keys():
            return ad
        raise Exception("Adicion no disponible")

    def precioServicio(self):
        return self.adiciones[self.ad]

    def __init__(self, ad):
        self.adiciones = {                               #Se establecen los precios de las adiciones
            "extraqueso": 4000,
            "gaseosa": 2000,
            "papas": 5000
        }
        self.ad = self.validarServicio(ad)


class Ingrediente:

    def validarValor(self, valor):                      #valida que los valores pertenezacan al tipo correcto de datos
        if valor in self.valores_permitidos.keys():
            return valor
        raise Exception("Sabor incorrecto")

    def calcularPrecio(self):
        return self.valores_permitidos[self.valor]

    def __init__(self, valor):
        self.valores_permitidos = {                    #Se establecen los precios de los ingredientes
            "pepperoni": 8000,
            "pollo-tocineta": 9000,
            "hawaiana": 8000,
            "carnes": 10000
        }
        self.valor = self.validarValor(valor)


class Pizza:

    def __init__(self, masa, tipo, ingredientes, adiciones):
        ##Tamaño->Str: s,m,l
        ##ingredientes->array
        ##masa->gruesa,delgada,media
        self.masa = Masa(masa, tipo)
        self.ingredientes = [Ingrediente(i) for i in ingredientes]
        self.adiciones = [Servicio(i) for i in adiciones]
        # self.adicion=[Servicio(i) for i in adiciones]

    def calcularPrecio(self):                           #Calcula el precio de final de la pizza
        costoingredientes = 0.0
        for ing in self.ingredientes:
            costoingredientes += ing.calcularPrecio()
        costomasa = self.masa.calcularPrecioMasa()
        costoservicio = 0.0
        for ad in self.adiciones:
            costoservicio += ad.precioServicio()
        return costoingredientes + costomasa + costoservicio


def main():
    orden = input("¿Desea crear una orden?: si o no ")
    while orden != "no":
        tamaño = input("Ingrese el tamaño: pequeña (p), mediana(m), large (l) ")
        tipo = input("Ingrese el tipo de masa: delgada (d), mediana (m), grande (g) ")
        ingredientes = input("Ingrese el sabor de la pizza: pepperoni, pollo-tocineta, hawaiana, carnes").split()
        adiciones = input("Ingrese las adiciones: extraqueso, gaseosa, papas").split()
        p1 = Pizza(tamaño, tipo, ingredientes, adiciones)
        total = p1.calcularPrecio()
        print(total)
        orden = input("¿Desea crear una orden?: si o no ")
main()