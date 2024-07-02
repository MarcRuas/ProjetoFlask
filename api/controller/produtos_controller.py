from flask import Blueprint, jsonify, request  # Importa os módulos necessários do Flask
from flask.views import MethodView  # Importa a classe base MethodView para visualizações baseadas em classes

# Cria um blueprint chamado 'produtos_controller' para organizar o código em módulos
produtos_controller_bp = Blueprint('produtos_controller', __name__)

# Define uma classe ProdutosController que herda de MethodView
class ProdutosController(MethodView):
    # Define o método GET para a rota
    def get(self):
        # Cria uma resposta com um produto de exemplo
        response = {
            'id': 1,
            'produto': 'Macarrao'
        }
        # Retorna a resposta como JSON com status HTTP 201 (Created)
        return jsonify(response), 201
    
    # Define o método POST para a rota
    def post(self):
        # Obtém os dados do formulário da requisição (produto e id)
        new_product = request.form.get('produto'), request.form.get('id')
        # Cria uma resposta com uma mensagem de sucesso e os dados do novo produto
        response = {
            'message': 'Produto criado com sucesso',
            'data': new_product
        }
        # Retorna a resposta como JSON com status HTTP 201 (Created)
        return jsonify(response), 201
    
# Adiciona uma regra de URL ao blueprint
produtos_controller_bp.add_url_rule(
    '/produtos',  # Define a rota
    view_func=ProdutosController.as_view('produtos')  # Associa a classe ProdutosController à rota usando as_view
)
