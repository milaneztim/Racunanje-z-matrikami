import bottle
import model

racun = model.Racun()


@bottle.get('/')
def index():
    return bottle.template('base.tpl')


@bottle.post('/igra/')
def nova_igra():
    id_igre = racun.nova_matrika()
    bottle.redirect('/igra/{}'.format(id_igre))


@bottle.get('/igra/<id_igre:int>/')
def pokazi_igro(id_igre):
    return bottle.template()


@bottle.get('/igra/<id_igre:int>/')
def zahtevaj velikost(id_igre):
    bottle.request.forms()

bottle.run(reloader=True, debug=True)
