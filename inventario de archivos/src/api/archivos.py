from flask import Flask, Blueprint,  redirect, request, jsonify, json, session, render_template
from common.Toke import *
from config.db import db, app, ma
from Model.Archivos import Arkive, ArkiveSchema

routes_files = Blueprint("routes_files", __name__)

ark_schema = ArkiveSchema()
Arkive_Schema = ArkiveSchema(many=True)

@routes_files.route('/files', methods=['GET'])
def obtenerfiles():    
    returnall = Arkive.query.all()
    result_arkive = Arkive_Schema.dump(returnall)
    return jsonify(result_arkive)


#<--------------------------CRUD FILES--------------------------->
@routes_files.route('/eliminarfiles/<id>', methods=['GET'] )
def eliminarfiles(id):
    act = Arkive.query.get(id)
    db.session.delete(act)
    db.session.commit()
    return jsonify(Arkive_Schema.dump(act))

@routes_files.route('/actualizarfiles', methods=['POST'] )
def actualizarfiles():
    id = request.json['id']
    nombreArchivo = request.json['nombreArchivo']
    tipo_archivo = request.json['tipo_archivo']
    ubicacion = request.json['ubicacion']
    fecha_creacion = request.json['fecha_creacion']
    fecha_modificacion = request.json['fecha_modificacion']
    id_etiqueta = request.json['id_etiqueta']
    id_usuarios = request.json['id_usuarios']
    comentarios = request.json['comentarios']
    ract = Arkive.query.get(id)
    ract.nombreArchivo = nombreArchivo
    ract.tipo_archivo = tipo_archivo
    ract.ubicacion = ubicacion
    ract.fecha_creacion = fecha_creacion
    ract.fecha_modificacion = fecha_modificacion
    ract.id_etiqueta = id_etiqueta
    ract.id_usuarios = id_usuarios
    ract.comentarios = comentarios
    
    db.session.commit()
    return redirect('/actividades')

@routes_files.route('/savefiles', methods=['POST'] )
def guardar_files():
    act = request.json['id', 'nombreArchivo', 'tipo_archivo', 
                       'ubicacion', 'fecha_creacion', 'fecha_modificacion',
                       'id_etiqueta', 'id_usuarios', 'comentarios']
    new_ark = Arkive(act)
    db.session.add(new_ark)
    db.session.commit()
    return redirect('/actividades')
