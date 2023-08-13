from flask import Flask,  redirect, request, jsonify, json, session, render_template, Blueprint
from config.db import db, app, ma



#importar routes 
from api.roles import routes_roles
from api.etiquets import routes_tag
from api.user import routes_user
from api.archivos import routes_files
from api.actividades import routes_actividades
from api.algo import routes_algo

#rutas


#ubicacion del api 
app.register_blueprint(routes_roles, url_prefix="/api")
app.register_blueprint(routes_tag, url_prefix="/api")
app.register_blueprint(routes_user, url_prefix="/api")
app.register_blueprint(routes_files,  url_prefix="/api")
app.register_blueprint(routes_actividades,  url_prefix="/api")
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
    
