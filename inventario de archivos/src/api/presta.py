from flask import Flask, Blueprint,  redirect, request, jsonify, json, session, render_template
from common.Toke import *
from config.db import db, app, ma
from Model.Prestamos import Prestamos, PrestamoSchema

routes_prestamos = Blueprint("routes_prestamos", __name__)

pres_schema = PrestamoSchema()
Presta_Schema = PrestamoSchema(many=True)

#Datos de la tabla actividades
@routes_prestamos.route('/prestamo', methods=['GET'])
def obteneractivity():    
    returnall = Prestamos.query.all()
    result_act = Presta_Schema.dump(returnall)
    return jsonify(result_act)


#<--------------------------CRUD ACTIVITY--------------------------->
@routes_prestamos.route('/eliminarpres/<id>', methods=['GET'] )
def eliminactivity(id):
    act = Prestamos.query.get(id)
    db.session.delete(act)
    db.session.commit()
    return jsonify(Presta_Schema.dump(act))

@routes_prestamos.route('/actualizarpres', methods=['POST'] )
def actualizaractivity():
    id = request.json['id']
    nombre = request.json['nombre']
    descripcion = request.json['descripcion']
    can_disponible = request.json['can_disponible']
    can_total = request.json['can_total']
    fecha_adquisicion = request.json['fecha_adquisicion']
    id_categoria = request.json['id_categoria']
    ract = Prestamos.query.get(id)
    ract.nombre = nombre
    ract.descripcion = descripcion
    ract.can_disponible = can_disponible
    ract.can_total = can_total
    ract.fecha_adquisicion = fecha_adquisicion
    ract.id_categoria = id_categoria
    
    db.session.commit()
    return redirect('/actividades')

@routes_prestamos.route('/savepres', methods=['POST'] )
def guardar_activity():
    act = request.json['nombre', 'descripcion', 'can_disponible', 'can_total', 'fecha_adquisicion', 'id_categoria']
    new_act = Prestamos(act)
    db.session.add(new_act)
    db.session.commit()
    return redirect('/prestamos')
