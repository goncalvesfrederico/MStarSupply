from flask import request, jsonify
from models import Local
from utils.utils import error_msg
from app import db

def get_location():
    locais = Local.query.all()
    result = [local.to_json() for local in locais]
    return jsonify(result)

def create_location():
    try:
        data = request.json
        
        # validation if the fields are empty!
        required_fields = ["nome", "endereco"]
        for field in required_fields:
            if field not in data or not data.get(field):
                return jsonify(
                    {
                        'error': f"Campo Obrigatótio: {field}",
                    }
                ), 400
            
        nome = data.get("nome")
        endereco = data.get("endereco")
        new_local = Local(
            nome=nome,
            endereco=endereco,
        )
        db.session.add(new_local)
        db.session.commit()
        return jsonify(new_local.to_json()), 201

    except Exception as e:
        db.session.rollback()
        return jsonify(error_msg(e)), 500
    
def delete_location(id):
    try:
        local = Local.query.get(id)
        if local is None:
            return jsonify(
                {
                    "error": "Local não encontrado"
                }
            )
        local_nome = local.nome
        db.session.delete(local)
        return jsonify(
            {
                "msg": f"Local {local_nome} foi excluido!"
            }
        )
    except Exception as e:
        db.session.rollback()
        return jsonify(error_msg(e)), 500
    
def update_location(id):
    try:
        local = Local.query.get(id)
        if local is None:
            return jsonify(
                {
                    "error": "Local não encontrado"
                }
            )
        
        data = request.json
        # validation if the fields is empty!
        required_fields = ["nome", "endereco"]
        for field in required_fields:
            if field not in data or not data.get(field):
                return jsonify(
                    {
                        'error': f"Campo Obrigatótio: {field}",
                    }
                ), 400
            
        local.nome = data.get("nome", local.nome)
        local.endereco = data.get("endereco", local.endereco)
        db.session.commit()
        return jsonify(local.to_json()), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify(error_msg(e)), 500