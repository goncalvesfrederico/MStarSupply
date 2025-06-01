from flask import request, jsonify
from models import TipoMovimentacao
from utils.utils import error_msg
from app import db

def get_movement_type():
    tipo_movimentacao = TipoMovimentacao.query.all()
    result = [tipo.to_json() for tipo in tipo_movimentacao]
    return jsonify(result)

def create_movement_type():
    try:
        data = request.get_json() or {}
        
        # validation if the fields is empty!
        required_fields = ["nome"]
        for field in required_fields:
            if not data.get(field):
                return jsonify(
                    {
                        "error": f"Campo Obrigatótio: {field}"
                    }
                ), 404
            
        nome = data.get("nome")
        new_tipo_movimentacao = TipoMovimentacao(
            nome=nome,
        )
        db.session.add(new_tipo_movimentacao)
        db.session.commit()
        return jsonify(new_tipo_movimentacao.to_json()), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify(error_msg(e)), 500 

def delete_movement_type(id):
    try:
        tipo_movimentacao = TipoMovimentacao.query.get(id)
        if tipo_movimentacao is None:
            return jsonify(
                {
                    "error": "Tipo de Movimentacao nao encontrado!"
                }
            ), 404
        
        tipo_movimentacao_nome = tipo_movimentacao.nome
        db.session.delete(tipo_movimentacao)
        db.session.commit()
        return jsonify(
            {
                "msg": f"Usuario {tipo_movimentacao_nome} deletado!"
            }
        ), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify(error_msg(e)), 500 

def update_movement_type(id):
    try:
        tipo_movimentacao = TipoMovimentacao.query.get(id)
        if tipo_movimentacao is None:
            return jsonify(
                {
                    "error": "Tipo de Movimentacao nao encontrado!"
                }
            ), 404
        
        data = request.get_json() or {}
        
        # validation if the fields is empty!
        required_fields = ["nome"]
        for field in required_fields:
            if not data.get(field):
                return jsonify(
                    {
                        "error": f"Campo Obrigatótio: {field}"
                    }
                ), 404
            
        tipo_movimentacao.nome = data.get("nome", tipo_movimentacao.nome)
        db.session.commit()
        return jsonify(tipo_movimentacao.to_json()), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify(error_msg(e)), 500 