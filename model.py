import Operacije
import tekstovni_vmesnik

ZACETEK = 'S'


class Matrika:

    def __init__(self, seznam):
        self.sez = seznam

    def __add__(self, other):
        return Operacije.vsota(self.sez, other.sez)

    def __sub__(self, other):
        return Operacije.vsota(self.sez, Operacije.mnozenje_s_skalarjem(other.sez, -1))

    def __mul__(self, other):
        if type(other) is int:
            return Operacije.mnozenje_s_skalarjem(self.sez, other)
        else:
            return Operacije.produkt(self.sez, other.sez)

    def __pow__(self, potenca):
        return Operacije.potenca(self.sez, potenca)

    def det(self):
        return Operacije.determinanta(self.sez)

    def transpose(self):
        return Operacije.transponirano(self.sez)

    def tr(self):
        return Operacije.sled(self.sez)

    def hadamard_product(self, other):
        return Operacije.hadamardov_produkt(self.sez, other.sez)


class Racun:

    def __init__(self):
        self.igre = {}

    def prost_id_igre(self):
        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys()) + 1

    def nova_matrika(self):
        matrika = tekstovni_vmesnik.pozeni_vmesnik()
        id_igre = self.prost_id_igre()
        self.igre[id_igre] = (matrika, ZACETEK)
        return id_igre
