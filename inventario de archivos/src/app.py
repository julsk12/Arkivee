from flask import Flask,  redirect, request, jsonify, json, session, render_template, Blueprint
from config.db import db, app, ma



#importar routes 
from api.roles import routes_roles
from api.categoria import routes_category
from api.user import routes_user
from api.obj import routes_obj
from api.prov import routes_prov
from api.presta import routes_prestamos
from api.de_prov import routes_det
from api.algo import routes_algo

#rutas


#ubicacion del api 
app.register_blueprint(routes_roles, url_prefix="/api")
app.register_blueprint(routes_category, url_prefix="/api")
app.register_blueprint(routes_user, url_prefix="/api")
app.register_blueprint(routes_obj,  url_prefix="/api")
app.register_blueprint(routes_prov,  url_prefix="/api")
app.register_blueprint(routes_prestamos,  url_prefix="/api")
app.register_blueprint(routes_det,  url_prefix="/api")
app.register_blueprint(routes_algo,  url_prefix="/api")



#------------------------------------------------
@app.route("/")
def index():
    titulo= "Pagina Princiapl"
    return "render_template('/main/login.html', titles=titulo)"

@app.route("/algo")
def otr():
    return "hola mundo"


# Datos de la tabla de Editoriales
if __name__ == '__main__':
   # load_dotenv()
    app.run(debug=True, port=5000, host='0.0.0.0')
    
