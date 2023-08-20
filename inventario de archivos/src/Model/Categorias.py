from config.db import db, app, ma 

class Categorias(db.Model):
    __tablename__ = "tblcategorias"

    
    id  = db.Column(db.Integer, primary_key=True)
    Nombre_categoria = db.Column(db.String(50))
    Description = db.Column(db.String(50))

    def __init__(self, Nombre_categoria,Description):
        self.Nombre_categoria = Nombre_categoria
        self.Description = Description
    
with app.app_context():
    db.create_all()

class CategoriasSchema(ma.Schema):
    class Meta:
        fields = ('id','Nombre_categoria','Description')
        