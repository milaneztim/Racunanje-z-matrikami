import bottle
import model


racun = model.Racun()


@bottle.get('/')
def index():
    return bottle.template('base.tpl')


@bottle.post('/vnos-dimenzije/<ime_matrike>')
def vnos_dimenzije(ime_matrike):
    return bottle.template('vnos-dimenzije.tpl', ime_matrike=ime_matrike)


@bottle.post('/vnos-matrike/<ime_matrike>')
def vnos_matrike(ime_matrike):
    podatki = bottle.request.forms

    try:
        m = int(podatki.get("m"))
    except:
        m = 1
    try:
        n = int(podatki.get("n"))
    except:
        n = 1
    racun.shrani_dimenzije(ime_matrike, m, n)
    return bottle.template('vnos-matrike.tpl', m=m, n=n, ime_matrike=ime_matrike)


@bottle.get('/izberi-operacijo/')
def izberi_operacijo():
    return bottle.template('izberi-operacijo.tpl')


# shranjevanje vpisanih podatkov, sem pripelje gumb Shrani matriko
@bottle.post('/dodaj-matriko/<ime_matrike>')
def dodaj_matriko(ime_matrike):
    podatki = bottle.request.forms
    m = racun.dimenzije[ime_matrike][0]
    n = racun.dimenzije[ime_matrike][1]

    matrika_seznam = []
    for i in range(m):
        vrstica = []
        for j in range(n):
            element = podatki.get('{}x{}'.format(i, j))
            try:
                element = float(element)
            except:
                element = 0
            vrstica.append(element)
        matrika_seznam.append(vrstica)
    racun.shrani_matriko(ime_matrike, matrika_seznam)
    return bottle.redirect('/izberi-operacijo/')


bottle.run(reloader=True, debug=True)
