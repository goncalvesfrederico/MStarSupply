from flask import request, jsonify
from models import Fabricante
from utils.utils import error_msg
from app import db

def get_manufacturer():
    fabricantes = Fabricante.query.all()
    result = [fabricante.to_json() for fabricante in fabricantes]
    return jsonify(result)

def create_manufacturer():
    try:
        data = request.json

        #  validation if the fields are empty
        required_fields = ["nome"]
        for field in required_fields:
            if field not in data or not data.get(field):
                return jsonify(
                    {
                        "error": f"Campo Obrigatório: {field}"
                    }
                ), 400

        nome = data.get("nome")
        new_fabricante = Fabricante(
            nome=nome,
        )    
        db.session.add(new_fabricante)
        db.session.commit()
        return jsonify(new_fabricante.to_json())
        
    except Exception as e:
        db.session.rollback()
        return jsonify(error_msg(e)), 500
    
def delete_manufacturer(id):
    try:
        fabricante = Fabricante.query.get(id)
        if fabricante is None:
            return jsonify(
                {
                    "error": "Fabricante não encontrado",
                }
            ), 404
        nome_fabricante = fabricante.nome
        db.session.delete(fabricante)
        db.session.commit()
        return jsonify(
            {
                "msg": f"Fabricante {nome_fabricante} excluido!"
            }
        ), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify(error_msg(e)), 500
    
def update_manufacturer(id):
    try:
        fabricante = Fabricante.query.get(id)
        if fabricante is None:
            return jsonify(
                {
                    "error": "Fabricante não encontrado",
                }
            ), 404
        
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

        fabricante.nome = data.get("nome", fabricante.nome)
        db.session.commit()
        return jsonify(fabricante.to_json()),200
    
    except Exception as e:
        db.session.rollback()
        return jsonify(error_msg(e)), 500