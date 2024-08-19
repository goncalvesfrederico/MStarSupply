from app import db
from datetime import datetime

class Fabricante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    mercadorias = db.relationship("Mercadoria", backref="fabricante")

    def to_json(self):
        return {
            "id": self.id,
            "nome": self.nome,
        }


class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    mercadorias = db.relationship("Mercadoria", backref="categoria")

    def to_json(self):
        return {
            "id": self.id,
            "nome": self.nome
        }


class Mercadoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    numero_registro = db.Column(db.String(50), nullable=False, unique=True)
    descricao = db.Column(db.Text, nullable=True)
    estoque = db.Column(db.Integer, nullable=False, default=0)
    fabricante_id = db.Column(db.Integer, db.ForeignKey("fabricante.id"), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey("categoria.id"), nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "numeroRegistro": self.numero_registro,
            "descricao": self.descricao,
            "estoque": self.estoque,
            "fabricanteId": self.fabricante_id,
            "categoriaId": self.categoria_id,
        }


class Local(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(200), nullable=True)
    followups = db.relationship("FollowUp", backref="local")

    def to_json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "endereco": self.endereco,
        }


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    user = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    group = db.Column(db.String(50), nullable=False)
    followups = db.relationship("FollowUp", backref="user")


class TipoMovimentacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    followups = db.relationship("FollowUp", backref="tipomovimentacao")


class FollowUp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo_movimentacao_id = db.Column(db.Integer, db.ForeignKey('tipo_movimentacao.id'), nullable=False)
    mercadoria_id = db.Column(db.Integer, db.ForeignKey('mercadoria.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    local_id = db.Column(db.Integer, db.ForeignKey('local.id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    data_movimento = db.Column(db.DateTime, default=datetime, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "tipoMovimentacaoId": self.tipo_movimentacao_id,
            "mercadoriaId": self.mercadoria_id,
            "userId": self.user_id,
            "localId": self.local_id,
            "quantidade": self.quantidade,
            "dataMovimento": self.data_movimento,
        }