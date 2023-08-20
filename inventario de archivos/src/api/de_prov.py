from flask import Flask, Blueprint,  redirect, request, jsonify, json, session, render_template
from common.Toke import *
from config.db import db, app, ma
from Model.Deta_obj import DetaProv, DProvSchema

routes_det = Blueprint("routes_det", __name__)

dop_schema = DProvSchema()
Dobp_Schema = DProvSchema(many=True)

@routes_det.route('/detallesp', methods=['GET'])
def obtenerdp():    
    returnall = DetaProv.query.all()
    result_arkive = Dobp_Schema.dump(returnall)
    return jsonify(result_arkive)


#<--------------------------CRUD FILES--------------------------->
@routes_det.route('/eliminardp/<id>', methods=['GET'] )
def eliminardp(id):
    act = DetaProv.query.get(id)
    db.session.delete(act)
    db.session.commit()
    return jsonify(Dobp_Schema.dump(act))

@routes_det.route('/actualizardp', methods=['POST'] )
def actualizardp():
    id = request.json['id']
    can_obj = request.json['can_obj']
    id_objeto = request.json['id_objeto']
    id_prove = request.json['id_prove']

    ract = DetaProv.query.get(id)
    ract.can_obj = can_obj
    ract.id_objeto = id_objeto
    ract.id_prove = id_prove

    
    db.session.commit()
    return redirect('/detallesp')

@routes_det.route('/saveodp', methods=['POST'] )
def guardar_dp():
    act = request.json['id', 'can_obj', 'id_objeto', 
                       'id_prove']
    new_ark = DetaProv(act)
    db.session.add(new_ark)
    db.session.commit()
    return redirect('/detallesp')
