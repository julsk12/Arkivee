from datetime import datetime
from common.Toke import *
from config.db import db, app, ma
from flask import (
    Flask,
    Blueprint,
    redirect,
    request,
    jsonify,
    json,
    session,
    render_template,
)
from Model.Usuarios import Users, UsuariosSchema

now = datetime.now()
routes_user = Blueprint("routes_user", __name__)

# usuario
Usuario_Schema = UsuariosSchema()
Usuarios_Schema = UsuariosSchema(many=True)


@routes_user.route("/Usuarios", methods=["GET"])
def usuarios():
    returnall = Users.query.all()
    resultado_usuarios = Usuarios_Schema.dump(returnall)
    return jsonify(resultado_usuarios)


# crud de usuarios
@routes_user.route("/eliminar_Users/<id>", methods=["GET"])
def eliminar_users(id):
    id_user = Users.query.get(id)
    db.session.delete(id_user)
    db.session.commit()
    return jsonify(UsuariosSchema.dump(id_user))


@routes_user.route("/actualizarUsers", methods=["POST"])
def actualizar_users():
    id = request.json["id"]
    nombre = request.json["nombre"]
    correo = request.json["correo"]
    password = request.json["password"]
    sede = request.json["sede"]
    users = Users.query.get(id)
    users.nombre = nombre
    users.correo = correo
    users.password = password
    users.sede = sede
    db.session.commit()
    return redirect("/Usuarios")


@routes_user.route("/save_Users", methods=["POST"])
def guardar_Users():
    usuarios = request.json["id, nombre, correo, password, sede, id_roles"]
    print(usuarios)
    new_Users = Users(usuarios)
    db.session.add(new_Users)
    db.session.commit()
    return redirect("/Usuarios")
