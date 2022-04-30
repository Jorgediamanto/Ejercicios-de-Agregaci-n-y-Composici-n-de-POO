class Edificio:
    Ar = 1
    
    def __init__(self,edificio,empresa,ciudad,empleados):
        self.empresa = empresa
        self.ciudad = ciudad
        self.empleados = empleados
        self.edificio = edificio

    def __del__(self):
        if self.edificio == "A" or self.edificio == "B":
            if self.Ar !=0:
                print("Edificio "+self.edificio+" ha sido destruido!")
                print("El empleado "+self.empleados+" ha muerto!")

A = Edificio("A","YooHOO!","New York","Martin")
B = Edificio("B","YooHOO!","New York","Salim")
C = Edificio("C","YooHOO!","Los Ángeles","Xing")


print("Un meteorito ha caido en New York")
A.__del__()
A.Ar-=1

B.__del__()
B.Ar-=1























