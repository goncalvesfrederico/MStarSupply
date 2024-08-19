from flask import request, jsonify
from app import app, db
from utils.utils import error_msg
from models import Fabricante, Categoria, Mercadoria, Local, User, TipoMovimentacao, FollowUp

# Get Fabricante
@app.route("/api/fabricantes", methods=["GET"])
def get_fabricante():
    fabricantes = Fabricante.query.all()
    result = [fabricante.to_json() for fabricante in fabricantes]
    return jsonify(result)

# Create Fabricante
@app.route("/api/fabricantes", methods=["POST"])
def create_fabricante():
    try:
        data = request.json
        
        # validation if the fields is empty!
        required_fields = ["nome"]
        for field in required_fields:
            if field not in data or not data.get(field):
                return jsonify(
                    {
                        'error': f"Campo Obrigatótio: {field}",
                    }
                ), 400
        
        nome = data.get("nome")
        new_fabricante = Fabricante(
            nome=nome,
        )
        db.session.add(new_fabricante)
        db.session.commit()
        return jsonify(new_fabricante.to_json()), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify(error_msg(e)), 500

# Delete Fabricante
@app.route("/api/fabricantes/<int:id>", methods=["DELETE"])
def delete_fabricante(id):
    try:
        fabricante = Fabricante.query.get(id)
        nome_fabricante = fabricante.nome
        if fabricante is None:
            return jsonify(
                {
                    "error": "Fabricante não encontrado",
                }
            ), 404
        db.session.delete(fabricante)
        db.session.commit()
        return jsonify(
            {
                "msg": f"Fabricante {nome_fabricante} excluido!"
            }
        ), 200

    except Exception as e:
        db.session.rollback()
        return jsonify(
            {
                "error": str(e),
            }
        ), 500

# Update Fabricante
@app.route("/api/fabricantes/<int:id>", methods=["PATCH"])
def update_fabricante(id):
    try:
        fabricante = Fabricante.query.get(id)
        print(fabricante.nome)
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