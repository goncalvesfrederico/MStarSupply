from flask import request, jsonify
from app import app, db
from utils.utils import error_msg
from datetime import datetime
from models import Mercadoria, Local, User, TipoMovimentacao, FollowUp
from routes.manufacturer_routes import manufacturer_routes
from routes.category_routes import category_routes
from routes.product_routes import products_routes
from routes.movement_type_routes import movement_type_routes
from routes.location_routes import location_routes
from services.user.user_service import get_user, create_user, delete_user, update_user

app.register_blueprint(manufacturer_routes)
app.register_blueprint(category_routes)
app.register_blueprint(products_routes)
app.register_blueprint(movement_type_routes)
app.register_blueprint(location_routes)

# Get users
@app.route("/api/users", methods=["GET"])
def get_usuario():
    return get_user()

# Create user
@app.route("/api/users", methods=["POST"])
def create_usuario():
    return create_user()

# Delete user
@app.route("/api/users/<int:id>", methods=["DELETE"])
def delete_usuario(id):
    return delete_user(id)

# Update user
@app.route("/api/users/<int:id>", methods=["PATCH"])
def update_usuario(id):
    return update_user(id)
    
# Get Followup
@app.route("/api/followup", methods=["GET"])
def get_followup():
    movimentacoes = FollowUp.query.all()
    result = [movimentacao.to_json() for movimentacao in movimentacoes]
    return jsonify(result)

# Create Followup
@app.route("/api/followup", methods=["POST"])
def create_followup():
    try:
        data = request.get_json() or {}
        
        # validation if the fields is empty!
        required_fields = ["tipoMovimentacaoId", "mercadoriaId", "userId", "localId", "quantidade"]
        for field in required_fields:
            if field not in data or not data.get(field):
                return jsonify(
                    {
                        "error": f"Campo Obrigatótio: {field}"
                    }
                ), 400

        tipo_movimentacao_id = data.get("tipoMovimentacaoId")
        mercadoria_id = data.get("mercadoriaId")
        user_id = data.get("userId")
        local_id = data.get("localId")
        quantidade = data.get("quantidade")

        foreign_key_validations = {
            "tipo_movimentacao": TipoMovimentacao.query.get(tipo_movimentacao_id),
            "mercadoria": Mercadoria.query.get(mercadoria_id),
            "usuario": User.query.get(user_id),
            "local": Local.query.get(local_id)
        }

        for k, v in foreign_key_validations.items():
            if v is None:
                return jsonify(
                    {
                        "error": f"{k} nao encontrado"
                    }
                ), 404
        
        # verifica se o tipo de movimentacao [1 ou 2] e muda o estoque
        if tipo_movimentacao_id == 1:
            foreign_key_validations["mercadoria"].estoque += quantidade

        elif tipo_movimentacao_id == 2:
            if foreign_key_validations["mercadoria"].estoque < quantidade:
                return jsonify(
                    {
                        "error": "Estoque insuficiente"
                    }
                ), 404
            foreign_key_validations["mercadoria"].estoque -= quantidade
        
        else:
            return jsonify(
                {
                    "error": "Nao existe esse tipo de movimentacao"
                }
            )

        new_movimentacao = FollowUp(
            tipo_movimentacao_id=tipo_movimentacao_id,
            mercadoria_id=mercadoria_id,
            user_id=user_id,
            local_id=local_id,
            quantidade=quantidade,
            data_movimento=datetime.now(),
        )

        db.session.add(new_movimentacao)
        db.session.commit()
        return jsonify(new_movimentacao.to_json()), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify(error_msg(e)), 500 