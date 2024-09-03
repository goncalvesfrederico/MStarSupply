from flask import request, jsonify
from models import User
from utils.utils import error_msg
from app import db

def get_user():
    users = User.query.all()
    result = [user.to_json() for user in users]
    return jsonify(result)

def create_user():
    try:
        data = request.json

        # validation if the fields are empty!
        required_fields = ["nome", "email", "user", "password", "group"]
        for field in required_fields:
            if field not in data or not data.get(field):
                return jsonify(
                    {
                        "error": f"Campo Obrigatório: {field}",
                    }
                ), 400
            
        nome = data.get("nome")
        email = data.get("email")
        user = data.get("user")
        password = data.get("password")
        group = data.get("group")

        new_user = User(
            nome=nome,
            email=email,
            user=user,
            password=password,
            group=group
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_json())
    
    except Exception as e:
        db.session.rollback()
        return jsonify(error_msg(e)), 500
    
def delete_user(id):
    try:
        user = User.query.get(id)
        if user is None:
            return jsonify(
                {
                    "error": "Usuario não encontrado"
                }
            ), 404
        user_nome = user.nome
        db.session.delete(user)
        db.session.commit()
        return jsonify(
            {
                "msg": f"Usuario {user_nome} deletado!"
            }
        ), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify(error_msg(e)), 500
    
def update_user(id):
    try:
        user = User.query.get(id)
        if user is None:
            return jsonify(
                {
                    "error": "Usuario nao encontrado!"
                }
            ), 404
        
        data = request.json
        
        # validation if the fields is empty!
        required_fields = ["nome", "email", "user", "password", "group"]
        for field in required_fields:
            if field not in data or not data.get(field):
                return jsonify(
                    {
                        'error': f"Campo Obrigatótio: {field}",
                    }
                ), 400

        user.nome = data.get("nome", user.nome)
        user.email = data.get("email", user.email)
        user.user = data.get("user", user.user)
        user.password = data.get("password", user.password)
        user.group = data.get("group", user.group)
        
        db.session.commit()
        return jsonify(user.to_json()), 200

    except Exception as e:
        db.session.rollback()
        return jsonify(error_msg(e)), 500