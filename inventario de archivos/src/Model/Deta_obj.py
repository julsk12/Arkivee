from flask import Blueprint, request, jsonify, json
from common.Toke import *
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template 

class DetaProv(db.Model):
    __tablename__ = "tbldprov"

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    can_obj = db.Column(db.Integer)
    id_objeto = db.Column(db.Integer, db.ForeignKey('tblobjetos.id'))
    id_prove = db.Column(db.Integer, db.ForeignKey('tblprov.id'))


    def __init__(self, id, can_obj, id_objeto, id_prove):
        self.id = id
        self.can_obj = can_obj
        self.id_objeto = id_objeto
        self.id_prove = id_prove

        
    
    
    with app.app_context():
            db.create_all()
  

class DProvSchema(ma.Schema):
    class Meta:
        fields = ('id','can_obj', 'id_objeto', 'id_prove')
