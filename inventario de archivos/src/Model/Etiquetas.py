from flask import Blueprint, request, jsonify, json
from common.Toke import *
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template 


class tags(db.Model):
    __tablename__ = "tbletiquetas"

    id = db.Column(db.Integer, primary_key=True)
    nombre_etiqueta= db.Column(db.String(200))
    descripcion = db.Column(db.Text)

    def __init__(self, nombre_etiqueta, descripcion):
        self.nombre_etiqueta = nombre_etiqueta
        self.descripcion = descripcion
    
    
    with app.app_context():
            db.create_all()
  

class TagSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre_etiqueta', 'descripcion')