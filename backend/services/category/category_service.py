from flask import request, jsonify
from models import Categoria
from utils.utils import error_msg
from app import db

def get_category():
    categorias = Categoria.query.all()
    result = [categoria.to_json() for categoria in categorias]
    return jsonify(result)

def create_category():
    try:
        data = request.json

        # validatiion if the fields are empty!
        required_fields = ["nome"]
        for field in required_fields:
            if field not in data or not data.get("nome"):
                return jsonify(
                    {
                        "error": f"Campo Obrigatório: {field}"
                    }
                ), 400
            
        nome = data.get("nome")
        new_categoria = Categoria(
            nome=nome,
        )
        db.session.add(new_categoria)
        db.session.commit()
        return jsonify(new_categoria.to_json()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify(error_msg(e)), 500
    
def delete_category(id):
    try:
        categoria = Categoria.query.get(id)
        if categoria is None:
            return jsonify(
                {
                    "error": "Categoria não encontrado",
                }
            ), 404
        nome_categoria = categoria.nome
        db.session.delete(categoria)
        db.session.commit()
        return jsonify(
            {
                "msg": f"Fabricante {nome_categoria} excluido!"
            }
        ), 200

    except Exception as e:
        db.session.rollback()
        return jsonify(error_msg(e)), 500
    
def update_category(id):
    try:
        categoria = Categoria.query.get(id)
        if categoria is None:
            return jsonify(
                {
                    "error": "Categoria não encontrado."
                }
            )
        data = request.json

        # validation if the fields is empty!
        required_fields = ["nome"]
        for field in required_fields:
            if field not in data or not data.get(field):
                return jsonify(
                    {
                        'error': f"Campo Obrigatótio: {field}",
                    }
                ), 404
            
        categoria.nome = data.get("nome", categoria.nome)
        db.session.commit()
        return jsonify(categoria.to_json()),200

    except Exception as e:
        db.session.rollback()
        return jsonify(error_msg(e)), 500