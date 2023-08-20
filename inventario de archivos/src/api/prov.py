from flask import Flask, Blueprint,  redirect, request, jsonify, json, session, render_template
from common.Toke import *
from config.db import db, app, ma
from Model.Proveedores import Proveedores, ProvSchema

routes_prov = Blueprint("routes_prov", __name__)

prov_schema = ProvSchema()
Prove_Schema = ProvSchema(many=True)

#Datos de la tabla actividades
@routes_prov.route('/proveeedores', methods=['GET'])
def obtenerprov():    
    returnall = Proveedores.query.all()
    result_act = Prove_Schema.dump(returnall)
    return jsonify(result_act)


#<--------------------------CRUD ACTIVITY--------------------------->
@routes_prov.route('/eliminarprov/<id>', methods=['GET'] )
def eliminprov(id):
    act = Proveedores.query.get(id)
    db.session.delete(act)
    db.session.commit()
    return jsonify(Prove_Schema.dump(act))

@routes_prov.route('/actualizarprov', methods=['POST'] )
def actualizarprov():
    id = request.json['id']
    nombre = request.json['nombre']
    descripcion = request.json['descripcion']
    can_disponible = request.json['can_disponible']
    can_total = request.json['can_total']
    fecha_adquisicion = request.json['fecha_adquisicion']
    id_categoria = request.json['id_categoria']
    ract = Proveedores.query.get(id)
    ract.nombre = nombre
    ract.descripcion = descripcion
    ract.can_disponible = can_disponible
    ract.can_total = can_total
    ract.fecha_adquisicion = fecha_adquisicion
    ract.id_categoria = id_categoria
    
    db.session.commit()
    return redirect('/proveedores')

@routes_prov.route('/saveprov', methods=['POST'] )
def guardar_prov():
    act = request.json['nombre', 'descripcion', 'can_disponible', 'can_total', 'fecha_adquisicion', 'id_categoria']
    new_act = Proveedores(act)
    db.session.add(new_act)
    db.session.commit()
    return redirect('/proveedores')