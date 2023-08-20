from common.Toke import *
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template, Blueprint

class Prestamos(db.Model):
    __tablename__ = "tblprestamos"

    id = db.Column(db.Integer, primary_key=True)    
    id_objeto = db.Column(db.Integer, db.ForeignKey('tblobjetos.id'))
    solicitante = db.Column(db.String(200))
    id_usuarios = db.Column(db.String(200))
    fecha_prestamo = db.Column(db.DateTime, nullable=False)
    fecha_devolucion = db.Column(db.DateTime, nullable=False)

    def __init__(self, id_objeto, solicitante, fecha_prestamo, fecha_devolucion):
        self.id_objeto = id_objeto
        self.solicitante = solicitante
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
    
    
    with app.app_context():
            db.create_all()
  

class PrestamoSchema(ma.Schema):
    class Meta:
        fields = ('id','id_objeto', 'solicitante', 
                  'fecha_prestamo', 'fecha_devolucion')
