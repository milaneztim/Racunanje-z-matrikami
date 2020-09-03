import model


def dolzina_maksimalnega_clena(sez):
    m = len(sez)
    n = len(sez[0])
    najvecji = max([sez[i][j] for i in range(m) for j in range(n)])
    return len(str(najvecji))


def prikaz_matrike(sez):
    m = len(sez)
    n = len(sez[0])
    razmik = dolzina_maksimalnega_clena(sez)
    for i in range(m):
        vrstica = '|'
        for j in range(n):
            clen = sez[i][j]
            razlika = razmik - len(str(clen))
            for _ in range(razlika // 2 + 1):
                vrstica += ' '
            vrstica += str(clen)
            for _ in range(razlika // 2):
                vrstica += ' '
            if razlika % 2 == 1:
                vrstica += ' '
        print(vrstica + ' |')


def zahtevaj_velikost():
    return input("Stevilo vrstic: "), input("Stevilo stolpcev: ")


def zahtevaj_vnos(m, n):
    return [[int(input("a_{0},{1} = ".format(i, j))) for j in range(1, n+1)]
            for i in range(1, m+1)]


def pozeni_vmesnik():
    while True:
        m, n = zahtevaj_velikost()
        sez = zahtevaj_vnos(int(m), int(n))
        return sez


#a = pozeni_vmesnik()
#print(prikaz_matrike(a))
