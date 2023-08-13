from common.Toke import *
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template, Blueprint

class Acti(db.Model):
    __tablename__ = "tblactividades"

    id = db.Column(db.Integer, primary_key=True)    
    id_archivo = db.Column(db.Integer, db.ForeignKey('tblarchivos.id'))
    tipo_actividad = db.Column(db.String(200))
    id_usuarios = db.Column(db.String(200))
    fecha_actividad = db.Column(db.DateTime, nullable=False)

    def __init__(self, id_archivo, tipo_actividad, fecha_actividad, id_usuarios):
        self.id_archivo = id_archivo
        self.tipo_actividad = tipo_actividad
        self.fecha_actividad = fecha_actividad
        self.id_usuarios = id_usuarios
    
    
    with app.app_context():
            db.create_all()
  

class ActividadesSchema(ma.Schema):
    class Meta:
        fields = ('id','id_archivo', 'tipo_actividad', 
                  'fecha_actividad', 'id_usuarios')
