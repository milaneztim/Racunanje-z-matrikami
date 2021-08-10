import bottle
import model


racun = model.Racun()


@bottle.get('/')
def index():
    return bottle.template('index.tpl')


@bottle.post('/vnos-dimenzije/<ime_matrike>')
def vnos_dimenzije(ime_matrike):
    return bottle.template('vnos-dimenzije.tpl', ime_matrike=ime_matrike)


@bottle.post('/vnos-matrike/<ime_matrike>')
def prvi_vnos_matrike(ime_matrike):
    podatki = bottle.request.forms
    m = podatki.get("m")
    n = podatki.get("n")
    if m.isnumeric() and n.isnumeric():
        m = int(m)
        n = int(n)
        racun.shrani_dimenzije(ime_matrike, m, n)
        return bottle.template('vnos-matrike.tpl', m=m, n=n, ime_matrike=ime_matrike)
    else:
        return bottle.template('napaka-decimalno.tpl')


@bottle.get('/vnos-matrike/<ime_matrike>')
def drugi_vnos_matrike(ime_matrike):
    m = racun.dimenzije['B'][0]
    n = racun.dimenzije['B'][1]
    return bottle.template('vnos-matrike.tpl', m=m, n=n, ime_matrike=ime_matrike)


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
    if ime_matrike == 'A':
        return bottle.redirect('/izberi-operacijo/')
    else:
        return bottle.redirect('/rezultat/')


@bottle.get('/izberi-operacijo/')
def izberi_operacijo():
    return bottle.template('izberi-operacijo.tpl')


@bottle.post('/shrani-operacijo/')
def shrani_operacijo():
    operacija = bottle.request.forms.get("operacija")
    racun.shrani_operacijo('A', operacija)
    if operacija in ["det", "transpose", "trace"]:
        return bottle.redirect('/rezultat/')
    elif operacija in ["plus", "minus", "hadamard"]:
        m = racun.dimenzije['A'][0]
        n = racun.dimenzije['A'][1]
        racun.shrani_dimenzije('B', m, n)
        return bottle.redirect('/vnos-matrike/B')
    elif operacija in ["produkt"]:
        return bottle.redirect('/vnos-dimenzije-produkt/')
    elif operacija in ["potenca"]:
        return bottle.redirect('/vnos-potence/')


@bottle.get('/vnos-dimenzije-produkt/')
def vnos_dimenzije_produkt():
    n = racun.dimenzije['A'][1]
    return bottle.template('vnos-dimenzije-produkt.tpl', m=n)


@bottle.get('/vnos-potence/')
def vnos_potence():
    return bottle.template('vnos-potence.tpl')


@bottle.post('/shrani-potenco/')
def shrani_potenco():
    potenca = bottle.request.forms.get("potenca")
    if potenca.isnumeric() or potenca[1:].isnumeric():
        potenca = int(potenca)
        racun.shrani_matriko('B', potenca)
        return bottle.redirect('/rezultat/')
    return bottle.template('napaka-decimalno.tpl')
    


@bottle.get('/rezultat/')            
def izvedi_racun():
    operacija = racun.operacije['A']
    if operacija in ["plus", "minus", "hadamard", "produkt"]:
        m = racun.dimenzije['A'][0]
        n = racun.dimenzije['B'][1]
        rezultat = racun.izvedi_operacijo('A', operacija, 'B')
        racun.shrani_dimenzije('A', m, n)
        return bottle.template('rezultat.tpl', rezultat=rezultat, m=m, n=n)
    elif operacija in ["det", "trace"]:
        m = racun.dimenzije['A'][0]
        n = racun.dimenzije['A'][1]
        if m != n:
            return bottle.template('napaka-dimenzija.tpl')
        rezultat = racun.izvedi_operacijo('A', operacija)
        return bottle.template('rezultat-skalar.tpl', rezultat=rezultat)
    elif operacija in ["transpose"]:
        m = racun.dimenzije['A'][1]
        n = racun.dimenzije['A'][0]
        rezultat = racun.izvedi_operacijo('A', operacija)
        racun.shrani_dimenzije('A', m, n)
        return bottle.template('rezultat.tpl', rezultat=rezultat, m=m, n=n)
    elif operacija in ["potenca"]:
        m = racun.dimenzije['A'][0]
        n = racun.dimenzije['A'][1]
        potenca = racun.matrike['B'].sez
        if m != n:
            return bottle.template('napaka-dimenzija.tpl')
        if potenca < 0 and racun.izvedi_operacijo('A', 'det') == 0:
            return bottle.template('napaka-izrojena.tpl')
        rezultat = racun.izvedi_operacijo('A', operacija, 'B')
        return bottle.template('rezultat.tpl', rezultat=rezultat, m=m, n=n)


@bottle.get('/img/<picture>')
def serve_pictures(picture):
    return bottle.static_file(picture, root='img')


bottle.run(reloader=True, debug=True)
