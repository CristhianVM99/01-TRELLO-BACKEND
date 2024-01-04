from flask import Flask

app = Flask(__name__)

# TODO: pagina principal.
@app.route('/')
def index():
    return "<h1>Bienvenido a la pagina principal.</h1>"

# TODO: pagina de contacto.
@app.route('/Contact')
def contacto():
    return "<h1>Contacte con Nosotros.</h1>"

# TODO: pagina sobre nosotros.
@app.route('/SobreNosotros')
def sobreNosotros():
    return "<h1>Información sobre la app.</h1>"