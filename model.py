import Operacije

class Matrika:

    def __init__(self, seznam):
        self.seznam = seznam
    
    def __add__(self, other):
        return Operacije.vsota(self.seznam, other.seznam)

    def __sub__(self, other):
        return Operacije.vsota(self.seznam, Operacije.mnozenje_s_skalarjem(other.seznam, -1))

    def __mul__(self, other):
        if type(other) is int:
            return Operacije.mnozenje_s_skalarjem(self.seznam, other)
        else:
            return Operacije.produkt(self.seznam, other.seznam)

    def __pow__(self, potenca):
        return Operacije.potenca(self.seznam, potenca)

    def det(self):
        return Operacije.determinanta(self.seznam)
    
    def transpose(self):
        return Operacije.transponirano(self.seznam)
    
    def tr(self):
        return Operacije.sled(self.seznam)
    
    def hadamard_product(self, other):
        return Operacije.hadamardov_produkt(self.seznam, other.seznam)

