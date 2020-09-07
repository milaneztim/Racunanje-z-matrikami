import Operacije
import tekstovni_vmesnik


class Matrika:

    def __init__(self, seznam):
        self.sez = seznam

    def __add__(self, other):
        return Operacije.vsota(self.sez, other.sez)

    def __sub__(self, other):
        nasprotna_vrednost = Operacije.mnozenje_s_skalarjem(other.sez, -1)
        return Operacije.vsota(self.sez, nasprotna_vrednost)

    def __mul__(self, other):
        if type(other) is int:
            return Operacije.mnozenje_s_skalarjem(self.sez, other)
        else:
            return Operacije.produkt(self.sez, other.sez)

    def hadamard_product(self, other):
        return Operacije.hadamardov_produkt(self.sez, other.sez)

    def __pow__(self, potenca):
        return Operacije.potenca(self.sez, potenca)

    def det(self):
        return Operacije.determinanta(self.sez)

    def transpose(self):
        return Operacije.transponirano(self.sez)

    def tr(self):
        return Operacije.sled(self.sez)


class Racun:

    def __init__(self):
        self.dimenzije = {}
        self.matrike = {}

    def shrani_dimenzije(self, ime, m, n):
        self.dimenzije[ime] = [m, n]

    def shrani_matriko(self, ime, seznam):
        self.matrike[ime] = Matrika(seznam)

    def izvedi_operacijo(self, ime_prve, operacija, ime_druge=None):
        mat1 = self.matrike[ime_prve]
        if operacija == "potenca":
            return mat1 ** ime_druge
        mat2 = self.matrike[ime_druge]
        if operacija == "plus":
            return mat1 + mat2
        if operacija == "minus":
            return mat1 - mat2
        if operacija == "produkt":
            return mat1 * mat2
        if operacija == "hadamard":
            return mat1.hadamard_product(mat2)
        if operacija == "transpose":
            return mat1.transpose()
        if operacija == "det":
            return mat1.det()
        if operacija == "trace":
            return mat1.tr()
