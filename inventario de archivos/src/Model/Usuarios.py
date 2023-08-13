from flask import Blueprint, request, jsonify, json
from common.Toke import *
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template 

class Users(db.Model):
    __tablename__ = "tblusuarios"

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    nombre = db.Column(db.String(200))
    correo = db.Column(db.String(200))
    password = db.Column(db.String(200))
    sede = db.Column(db.String(200))
    id_roles = db.Column(db.Integer, db.ForeignKey('tblrolesusuario.id'))

    def __init__(self, id, nombre, correo, password, sede, id_roles):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.password = password
        self.sede = sede
        self.id_roles = id_roles
    
    
    with app.app_context():
            db.create_all()
  

class UsuariosSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre', 'correo', 'password',
                   'sede', 'id_roles')
