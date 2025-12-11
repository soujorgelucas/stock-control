from flask import Flask
from app.routes.produto_routes import produto_bp
from app.routes.categoria_routes import categoria_bp
from app.routes.fornecedor_routes import fornecedor_bp
from app.routes.movimentacao_routes import movimentacao_bp
from app import create_app

app = create_app()

# Registrar blueprints
app.register_blueprint(produto_bp, url_prefix="/produtos")
app.register_blueprint(categoria_bp, url_prefix="/categorias")
app.register_blueprint(fornecedor_bp, url_prefix="/fornecedores")
app.register_blueprint(movimentacao_bp, url_prefix="/movimentacoes")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
