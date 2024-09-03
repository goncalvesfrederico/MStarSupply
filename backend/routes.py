from flask import request, jsonify
from app import app, db
from utils.utils import error_msg
from datetime import datetime
from models import Mercadoria, Local, User, TipoMovimentacao, FollowUp
from services.manufacturer.manufacturer_service import get_manufacturer, create_manufacturer, delete_manufacturer, update_manufacturer
from services.category.category_service import get_category, create_category, delete_category, update_category
from services.products.products_service import get_products, create_products, delete_products, update_products
from services.location.location_service import get_location, create_location, delete_location, update_location
from services.user.user_service import get_user, create_user, delete_user, update_user

# Get Fabricante
@app.route("/api/fabricantes", methods=["GET"])
def get_fabricante():
    return get_manufacturer()

# Create Fabricante
@app.route("/api/fabricantes", methods=["POST"])
def create_fabricante():
    return create_manufacturer()

# Delete Fabricante
@app.route("/api/fabricantes/<int:id>", methods=["DELETE"])
def delete_fabricante(id):
    return delete_manufacturer(id)

# Update Fabricante
@app.route("/api/fabricantes/<int:id>", methods=["PATCH"])
def update_fabricante(id):
    return update_manufacturer(id)

# Get Categoria
@app.route("/api/categorias", methods=["GET"])
def get_categoria():
    return get_category()

# Create Categoria
@app.route("/api/categorias", methods=["POST"])
def create_categoria():
    return create_category()
    
# Delete Categoria
@app.route("/api/categorias/<int:id>", methods=["DELETE"])
def delete_categoria(id):
    return delete_category(id)

# Update Categoria
@app.route("/api/categorias/<int:id>", methods=["PATCH"])
def update_categoria(id):
    return update_category(id)
    
# Get Mercadoria
@app.route("/api/mercadorias", methods=["GET"])
def get_mercadorias():
    return get_products()

# Create Mercadoria
@app.route("/api/mercadorias", methods=["POST"])
def create_mercadoria():
    return create_products()

# Delete Mercadoria
@app.route("/api/mercadorias/<int:id>", methods=["DELETE"])
def delete_mercadoria(id):
    return delete_products(id)

# Update Mercadoria
@app.route("/api/mercadorias/<int:id>", methods=["PATCH"])
def update_mercadoria(id):
    return update_products(id)
    
# Get Local
@app.route("/api/locais", methods=["GET"])
def get_local():
    return get_location()

# Create Local
@app.route("/api/locais", methods=["POST"])
def create_local():
    return create_location()

# Delete Local
@app.route("/api/locais/<int:id>", methods=["DELETE"])
def delete_local(id):
    return delete_location(id)

# Update Local
@app.route("/api/locais/<int:id>", methods=["PATCH"])
def update_local(id):
    return update_location(id)
    
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
    
# Get Tipo da Movimentacao
@app.route("/api/tipomovimentacao", methods=["GET"])
def get_tipo_movimentacao():
    tipo_movimentacao = TipoMovimentacao.query.all()
    result = [tipo.to_json() for tipo in tipo_movimentacao]
    return jsonify(result)

# Create Tipo da Movimentacao
@app.route("/api/tipomovimentacao", methods=["POST"])
def create_tipo_movimentacao():
    try:
        data = request.json
        
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

# Delete Tipo da Movimentacao
@app.route("/api/tipomovimentacao/<int:id>", methods=["DELETE"])
def delete_tipo_movimentacao(id):
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

# Update Tipo da Movimentacao
@app.route("/api/tipomovimentacao/<int:id>", methods=["PATCH"])
def update_tipo_movimentacao(id):
    try:
        tipo_movimentacao = TipoMovimentacao.query.get(id)
        if tipo_movimentacao is None:
            return jsonify(
                {
                    "error": "Tipo de Movimentacao nao encontrado!"
                }
            ), 404
        
        data = request.json
        
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
        data = request.json
        
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