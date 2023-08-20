from flask import Blueprint, request, jsonify, json
from common.Toke import *
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template 

class Objetos(db.Model):
    __tablename__ = "tblobjetos"

    id = db.Column(db.Integer, primary_key=True)
    nombre= db.Column(db.String(200))
    descripcion = db.Column(db.Text)
    can_disponible = db.Column(db.Integer)
    can_total = db.Column(db.Integer)
    fecha_adquisicion = db.Column(db.DateTime, nullable=False)
    id_categoria = db.Column(db.Integer, db.ForeignKey('tblcategorias.id'))


    def __init__(self, nombre, descripcion, can_disponible, can_total, fecha_adquisicion, id_categoria):
        self.nombre = nombre
        self.descripcion = descripcion
        self.can_disponible = can_disponible
        self.can_total = can_total
        self.fecha_adquisicion = fecha_adquisicion
        self.id_categoria = id_categoria

    
    
    with app.app_context():
            db.create_all()
  

class ObjetoSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre', 'descripcion', 'can_disponible', 
                  'can_total', 'fecha_adquisicion', 'id_categoria')
