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
        return jsonify(error_msg(e))
    
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
        return jsonify(error_msg(e))

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
        return jsonify(error_msg(e))
    
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
        return jsonify(error_msg(e))

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
        return jsonify(error_msg(e))

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
        return jsonify(error_msg(e))
    
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
        return jsonify(error_msg(e))

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
        return jsonify(error_msg(e))

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
        return jsonify(error_msg(e))