from flask import Flask, Blueprint,  redirect, request, jsonify, json, session, render_template
from common.Toke import *
from config.db import db, app, ma
from Model.Objetos import Objetos, ObjetoSchema

routes_obj = Blueprint("routes_obj", __name__)

obj_schema = ObjetoSchema()
Object_Schema = ObjetoSchema(many=True)

@routes_obj.route('/objetos', methods=['GET'])
def obtenerobj():    
    returnall = Objetos.query.all()
    result_arkive = Object_Schema.dump(returnall)
    return jsonify(result_arkive)


#<--------------------------CRUD FILES--------------------------->
@routes_obj.route('/eliminarobject/<id>', methods=['GET'] )
def eliminarobj(id):
    act = Objetos.query.get(id)
    db.session.delete(act)
    db.session.commit()
    return jsonify(Object_Schema.dump(act))

@routes_obj.route('/actualizarobject', methods=['POST'] )
def actualizarobj():
    id = request.json['id']
    nombre = request.json['nombre']
    descripcion = request.json['descripcion']
    can_disponible = request.json['can_disponible']
    can_total = request.json['can_total']
    fecha_adquisicion = request.json['fecha_adquisicion']
    id_categoria = request.json['id_categoria']

    ract = Objetos.query.get(id)
    ract.nombre = nombre
    ract.descripcion = descripcion
    ract.can_disponible = can_disponible
    ract.can_total = can_total
    ract.fecha_adquisicion = fecha_adquisicion
    ract.id_categoria = id_categoria

    
    db.session.commit()
    return redirect('/activiobjetos')

@routes_obj.route('/saveobject', methods=['POST'] )
def guardar_obj():
    act = request.json['id', 'nombre', 'descripcion', 
                       'can_disponible', 'can_total', 'fecha_adquisicion',
                       'id_categoria']
    new_ark = Objetos(act)
    db.session.add(new_ark)
    db.session.commit()
    return redirect('/activiobjetos')
