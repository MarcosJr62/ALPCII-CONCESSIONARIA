from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Criação da aplicação Flask
app = Flask(__name__)

# Configuração do banco de dados MySQL (usando pymysql)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Gui2007*@localhost/concessionaria_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Criação do objeto db para SQLAlchemy
db = SQLAlchemy(app)

# Classe de modelo do veículo (usando POO com SQLAlchemy)
class Veiculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # ID único do veículo
    marca = db.Column(db.String(50), nullable=False)  # Marca do veículo
    modelo = db.Column(db.String(50), nullable=False)  # Modelo do veículo
    ano = db.Column(db.Integer, nullable=False)  # Ano do veículo
    _preco = db.Column(db.Float, nullable=False)  # Atributo privado para preço

    # Propriedade para acessar o preço (getter)
    @property
    def preco(self):
        return self._preco

    # Setter para validar o preço (não aceitar negativo)
    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError("Preço não pode ser negativo.")
        self._preco = valor

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para cadastrar veículo (GET mostra formulário, POST salva)
@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        try:
            # Recebe dados do formulário
            marca = request.form['marca']
            modelo = request.form['modelo']
            ano = int(request.form['ano'])
            preco = float(request.form['preco'])
            
            # Validação simples: campos obrigatórios
            if not marca or not modelo or ano <= 0:
                return "Erro: Campos obrigatórios não preenchidos ou ano inválido."
            
            # Cria veículo e salva no banco
            veiculo = Veiculo(marca=marca, modelo=modelo, ano=ano)
            veiculo.preco = preco  # Usa setter para validação
            db.session.add(veiculo)
            db.session.flush()  #Gartante que o veiculo.id exista
            registro = Historico(
                tipo='Cadastro',
                veiculo=f'{veiculo.marca} {veiculo.modelo} (id={veiculo.id})',
                 detalhes='Veículo cadastrado no sistema.'
            )
            db.session.add(registro)
            db.session.commit()
            return redirect(url_for('listar'))
        except ValueError as e:
            return f"Erro: {str(e)}"
        except Exception as e:
            return f"Erro ao cadastrar: {str(e)}"
    return render_template('cadastrar.html')

# Rota para listar veículos
@app.route('/listar')
def listar():
    veiculos = Veiculo.query.all()  # Busca todos os veículos
    return render_template('listar.html', veiculos=veiculos)
#Rota para abrir historico de acoes dentro do web
@app.route('/historico')
def historico():
    registros = Historico.query.order_by(Historico.data_hora.desc()).all()
    return render_template('historico.html', historicos=registros)



# Rota para editar veículo (GET mostra formulário preenchido, POST atualiza)
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    veiculo = Veiculo.query.get(id)  # Busca veículo por ID
    if not veiculo:
        return "Erro: Veículo não encontrado."
    
    if request.method == 'POST':
        try:
            # Recebe dados do formulário
            marca = request.form['marca']
            modelo = request.form['modelo']
            ano = int(request.form['ano'])
            preco = float(request.form['preco'])
            
            # Validação simples
            if not marca or not modelo or ano <= 0:
                return "Erro: Campos obrigatórios não preenchidos ou ano inválido."
            
            # Atualiza veículo
            veiculo.marca = marca
            veiculo.modelo = modelo
            veiculo.ano = ano
            veiculo.preco = preco  # Usa setter
            db.session.commit()
            return redirect(url_for('listar'))
        except ValueError as e:
            return f"Erro: {str(e)}"
        except Exception as e:
            return f"Erro ao editar: {str(e)}"
    return render_template('editar.html', veiculo=veiculo)

# Rota para excluir veículo
@app.route('/excluir/<int:id>')
def excluir(id):
    veiculo = Veiculo.query.get(id)  # Busca veículo por ID
    if not veiculo:
        return "Erro: Veículo não encontrado."
    try:
        registro = Historico(
        tipo='Exclusão',
        veiculo=f'{veiculo.marca} {veiculo.modelo} (id={veiculo.id})',
        detalhes='Veículo removido do sistema.'
        )
        db.session.add(registro)
        db.session.delete(veiculo)
        db.session.commit()
        return redirect(url_for('listar'))
    except Exception as e:
        return f"Erro ao excluir: {str(e)}"

#serve para criar a tabela historico no banco de dados se ainda nao existir
class Historico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(20), nullable=False)      
    veiculo = db.Column(db.String(100), nullable=False)  
    detalhes = db.Column(db.String(200), nullable=True)
    data_hora = db.Column(db.DateTime, default=datetime.utcnow)


# Bloco principal para rodar o app
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco se não existirem
    app.run(debug=True)