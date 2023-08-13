from flask import Blueprint, request, jsonify, json
from common.Toke import *
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template 

class Arkive(db.Model):
    __tablename__ = "tblarchivos"

    id = db.Column(db.Integer, primary_key=True)
    nombreArchivo= db.Column(db.String(200))
    tipo_archivo = db.Column(db.String(200))
    ubicacion = db.Column(db.String(500))
    fecha_creacion = db.Column(db.Date)
    fecha_modificacion = db.Column(db.DateTime, nullable=False)
    id_etiqueta = db.Column(db.Integer, db.ForeignKey('tbletiquetas.id'))
    id_usuarios = db.Column(db.Integer, db.ForeignKey('tblusuarios.id'))
    comentarios = db.Column(db.Text)

    def __init__(self, nombreArchivo, tipo_archivo, ubicacion, fecha_creacion, fecha_modificacion, id_etiqueta, id_usuarios, comentarios):
        self.nombreArchivo = nombreArchivo
        self.tipo_archivo = tipo_archivo
        self.ubicacion = ubicacion
        self.fecha_creacion = fecha_creacion
        self.fecha_modificacion = fecha_modificacion
        self.id_etiqueta = id_etiqueta
        self.id_usuarios = id_usuarios
        self.comentarios = comentarios
    
    
    with app.app_context():
            db.create_all()
  

class ArkiveSchema(ma.Schema):
    class Meta:
        fields = ('id','nombreArchivo', 'tipo_archivo', 'ubicacion', 
                  'fecha_creacion', 'fecha_modificacion', 'id_etiqueta', 'id_usuarios', 'comentarios')
