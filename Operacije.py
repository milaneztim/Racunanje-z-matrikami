def identiteta(n):
    rezultat = []
    for i in range(n):
        vrstica = []
        for j in range(n):
            if i == j:
                vrstica.append(1)
            else:
                vrstica.append(0)
        rezultat.append(vrstica)
    return rezultat


def vsota(mat1, mat2):
    m = len(mat1)
    n = len(mat1[0])
    return [[mat1[i][j] + mat2[i][j] for j in range(n)] for i in range(m)]


def mnozenje_s_skalarjem(mat, a):
    m = len(mat)
    n = len(mat[0])
    return [[mat[i][j] * a for j in range(n)] for i in range(m)]


def produkt(mat1, mat2):
    m = len(mat1)
    n = len(mat1[0])
    p = len(mat2[0])
    rezultat = []
    for i in range(m):
        vrstica = []
        for k in range(p):
            vsota = 0
            for j in range(n):
                vsota += mat1[i][j] * mat2[j][k]
            vrstica.append(vsota)
        rezultat.append(vrstica)
    return rezultat


def transponirano(mat):
    m = len(mat)
    n = len(mat[0])
    return [[mat[j][i] for j in range(m)] for i in range(n)]


def podmatrika(mat, i, j):
    return [vrstica[:j] + vrstica[j+1:] for vrstica in (mat[:i]+mat[i+1:])]


def determinanta(mat):
    n = len(mat)
    if n == 1:
        return mat[0][0]
    if n == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    else:
        razvoj_po_vrstici = 0
        for i in range(n):
            razvoj_po_vrstici += (-1) ** i * mat[0][i] * determinanta(podmatrika(mat, 0, i))
    return razvoj_po_vrstici


def inverz(mat):
    n = len(mat)
    prirejenka = [[(-1) ** (i + j) * determinanta(podmatrika(mat, i, j))
                  for j in range(n)] for i in range(n)]
    return mnozenje_s_skalarjem(transponirano(prirejenka), 1 / determinanta(mat))


def potenca(mat, k):
    n = len(mat)
    if k == 0:
        return identiteta(n)
    elif k == 1:
        return mat
    elif k < 0:
        return potenca(inverz(mat), abs(k))
    else:
        return potenca(produkt(mat, mat), k-1)


def sled(mat):
    n = len(mat)
    vsota = 0
    for i in range(n):
        vsota += mat[i][i]
    return vsota


def hadamardov_produkt(mat1, mat2):
    m = len(mat1)
    n = len(mat1[0])
    return [[mat1[i][j] * mat2[i][j] for j in range(n)] for i in range(m)]
