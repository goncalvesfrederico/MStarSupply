from flask import request, jsonify
from models import Mercadoria
from utils.utils import error_msg
from app import db

def get_products():
    products = Mercadoria.query.all()
    result = [product.to_json() for product in products]
    return jsonify(result)

def create_products():
    try:
        data = request.json

        # validation if the fields is empty!
        required_fields = ["nome", "numeroRegistro", "descricao", "estoque", "fabricanteId", "categoriaId"]
        for field in required_fields:
            if field not in data or not data.get(field):
                return jsonify(
                    {
                        'error': f"Campo Obrigatótio: {field}",
                    }
                ), 400
        
        nome = data.get("nome")
        numero_registro = data.get("numeroRegistro")
        descricao = data.get("descricao")
        estoque = data.get("estoque")
        fabricante_id = data.get("fabricanteId")
        categoria_id = data.get("categoriaId")

        new_mercadoria = Mercadoria(
            nome=nome,
            numero_registro=numero_registro,
            descricao=descricao,
            estoque=estoque,
            fabricante_id=fabricante_id,
            categoria_id=categoria_id
        )
        db.session.add(new_mercadoria)
        db.session.commit()
        return jsonify(new_mercadoria.to_json()), 201

    except Exception as e:
        db.session.rollback()
        return jsonify(error_msg(e)), 500
    
def delete_products(id):
    try:
        mercadoria = Mercadoria.query.get(id)
        if mercadoria is None:
            return jsonify(
                {
                    "error": "Mercadoria não encontrado"
                }
            ), 400
        nome_mercadoria = mercadoria.nome
        db.session.delete(mercadoria)
        db.session.commit()
        return jsonify(
            {
                "msg": f"Fabricante {nome_mercadoria} excluido!"
            }
        )
        
    except Exception as e:
        db.session.rollback()
        return jsonify(error_msg(e)), 500

def update_products(id):
    try:
        mercadoria = Mercadoria.query.get(id)
        if mercadoria is None:
            return jsonify(
                {
                    "error": "Mercadoria não encontrado."
                }
            )
        data = request.json

        # validation if the fields are empty!
        required_fields = ["nome", "numeroRegistro", "descricao", "estoque", "fabricanteId", "categoriaId"]
        for field in required_fields:
            if field not in data or not data.get(field):
                return jsonify(
                    {
                        "error": f"Campo Obrigatório: {field}",
                    }
                ), 404
            
        mercadoria.nome = data.get("nome", mercadoria.nome)
        mercadoria.numero_registro = data.get("numeroRegistro", mercadoria.numero_registro)
        mercadoria.descricao = data.get("descricao", mercadoria.descricao)
        mercadoria.estoque = data.get("estoque", mercadoria.estoque)
        mercadoria.fabricante_id = data.get("fabricanteId", mercadoria.fabricante_id)
        mercadoria.categoria_id = data.get("categoriaId", mercadoria.categoria_id)
        db.session.commit()
        return jsonify(mercadoria.to_json()), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify(error_msg(e)), 500