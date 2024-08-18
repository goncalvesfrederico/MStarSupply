from app import db

class Fabricante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)


class Mercadoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    numero_registro = db.Column(db.String(50), nullable=False, unique=True)
    descricao = db.Column(db.Text, nullable=True)
    estoque = db.Column(db.Integer, nullable=False, default=0)
    fabricante_id = db.Column(db.Integer, db.ForeignKey("fabricante.id"), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey("categoria.id"), nullable=False)


class Local(db.Model):
    ...


class User(db.Model):
    ...


class TipoMovimentacao(db.Model):
    ...


class FollowUp(db.Model):
    ...