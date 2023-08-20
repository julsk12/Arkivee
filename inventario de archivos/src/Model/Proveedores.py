from flask import Blueprint, request, jsonify, json
from common.Toke import *
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template 

class Proveedores(db.Model):
    __tablename__ = "tblprov"

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    nombre = db.Column(db.String(200))
    correo = db.Column(db.String(200))
    telefono = db.Column(db.Integer)
    direccion = db.Column(db.String(200))

    def __init__(self, id, nombre, correo, telefono, direccion):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
        
    
    
    with app.app_context():
            db.create_all()
  

class ProvSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre', 'correo', 'telefono',
                   'direccion')
