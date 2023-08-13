from flask import Flask, Blueprint,  redirect, request, jsonify, json, session, render_template
from common.Toke import *
from config.db import db, app, ma
from Model.Act import Acti, ActividadesSchema

routes_actividades = Blueprint("routes_actividades", __name__)

acti_schema = ActividadesSchema()
Activi_Schema = ActividadesSchema(many=True)

#Datos de la tabla actividades
@routes_actividades.route('/actividades', methods=['GET'])
def obteneractivity():    
    returnall = Acti.query.all()
    result_act = Activi_Schema.dump(returnall)
    return jsonify(result_act)


#<--------------------------CRUD ACTIVITY--------------------------->
@routes_actividades.route('/eliminaractivity/<id>', methods=['GET'] )
def eliminactivity(id):
    act = Acti.query.get(id)
    db.session.delete(act)
    db.session.commit()
    return jsonify(Activi_Schema.dump(act))

@routes_actividades.route('/actualizaractivity', methods=['POST'] )
def actualizaractivity():
    id = request.json['id']
    id_archivo = request.json['id_archivo']
    tipo_actividad = request.json['tipo_actividad']
    fecha_actividad = request.json['fecha_actividad']
    id_usuarios = request.json['id_usuarios']
    ract = Acti.query.get(id)
    ract.id_archivo = id_archivo
    ract.tipo_actividad = tipo_actividad
    ract.fecha_actividad = fecha_actividad
    ract.id_usuarios = id_usuarios
    
    db.session.commit()
    return redirect('/actividades')

@routes_actividades.route('/saveactivity', methods=['POST'] )
def guardar_activity():
    act = request.json['id_archivo', 'tipo_actividad', 'fecha_actividad', 'id_usuarios']
    new_act = Acti(act)
    db.session.add(new_act)
    db.session.commit()
    return redirect('/actividades')
