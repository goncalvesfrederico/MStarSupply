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

# Update Fabricante
@app.route("/api/fabricantes/<int:id>", methods=["PATCH"])
def update_fabricante(id):
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

# Get Categoria
@app.route("/api/categorias", methods=["GET"])
def get_categoria():
    categorias = Categoria.query.all()
    result = [categoria.to_json() for categoria in categorias]
    return jsonify(result)

# Create Categoria
@app.route("/api/categorias", methods=["POST"])
def create_categoria():
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
        new_categoria = Categoria(
            nome=nome,
        )
        db.session.add(new_categoria)
        db.session.commit()
        return jsonify(new_categoria.to_json()), 201

    except Exception as e:
        db.session.rollback()
        return jsonify(error_msg(e)), 500
    
# Delete Categoria
@app.route("/api/categorias/<int:id>", methods=["DELETE"])
def delete_categoria(id):
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

# Update Categoria
@app.route("/api/categorias/<int:id>", methods=["PATCH"])
def update_categoria(id):
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
    
# Get Mercadoria
@app.route("/api/mercadorias", methods=["GET"])
def get_mercadorias():
    mercadorias = Mercadoria.query.all()
    result = [mercadoria.to_json() for mercadoria in mercadorias]
    return jsonify(result)

# Create Mercadoria
@app.route("/api/mercadorias", methods=["POST"])
def create_mercadoria():
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

# Delete Mercadoria
@app.route("/api/mercadorias/<int:id>", methods=["DELETE"])
def delete_mercadoria(id):
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

# Update Mercadoria
@app.route("/api/mercadorias/<int:id>", methods=["PATCH"])
def update_mercadoria(id):
    try:
        mercadoria = Mercadoria.query.get(id)
        if mercadoria is None:
            return jsonify(
                {
                    "error": "Mercadoria não encontrado."
                }
            )
        data = request.json

        # validation if the fields is empty!
        required_fields = ["nome", "numeroRegistro", "descricao", "estoque", "fabricanteId", "categoriaId"]
        for field in required_fields:
            if field not in data or not data.get(field):
                return jsonify(
                    {
                        'error': f"Campo Obrigatótio: {field}",
                    }
                ), 404
            
        mercadoria.nome = data.get("nome", mercadoria.nome)
        mercadoria.numero_registro = data.get("numeroRegistro", mercadoria.numero_registro)
        mercadoria.descricao = data.get("descricao", mercadoria.descricao)
        mercadoria.estoque = data.get("estoque", mercadoria.estoque)
        mercadoria.fabricante_id = data.get("fabricanteId", mercadoria.fabricante_id)
        mercadoria.categoria_id = data.get("categoriaId", mercadoria.categoria_id)
        db.session.commit()
        return jsonify(mercadoria.to_json()),200
    except Exception as e:
        db.session.rollback()
        return jsonify(error_msg(e)), 500
    
# Get Local
@app.route("/api/locais", methods=["GET"])
def get_local():
    locais = Local.query.all()
    result = [local.to_json() for local in locais]
    return jsonify(result)

# Create Local
@app.route("/api/locais", methods=["POST"])
def create_local():
    try:
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

# Delete Local
@app.route("/api/locais/<int:id>", methods=["DELETE"])
def delete_local(id):
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

# Update Local
@app.route("/api/locais/<int:id>", methods=["PATCH"])
def update_local(id):
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
    
# Get users
@app.route("/api/users", methods=["GET"])
def get_users():
    users = User.query.all()
    result = [user.to_json() for user in users]
    return jsonify(result)

# Create user
@app.route("/api/users", methods=["POST"])
def create_user():
    try:
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

# Delete user
@app.route("/api/users/<int:id>", methods=["DELETE"])
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

# Update user
@app.route("/api/users/<int:id>", methods=["PATCH"])
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
                        "error": f"Missing required field: {field}"
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
                        "error": f"Missing required field: {field}"
                    }
                ), 404
            
        tipo_movimentacao.nome = data.get("nome", tipo_movimentacao.nome)
        db.session.commit()
        return jsonify(tipo_movimentacao.to_json()), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify(error_msg(e)), 500 