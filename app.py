from flask import Flask, jsonify, request
from database import db
from models.snack import Snack
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@127.0.0.1:3307/flask-crud-snack' # configuracao passar o caminho do banco de dados
db.init_app(app)


@app.route('/create/snack', methods=['POST'])
def create_snack(): 
  data = request.json

  name = data.get('name')
  diet = data.get('diet')
  description = data.get('description')

  snack = Snack(name=name, description=description, timestamp=datetime.today().date(), diet=diet)

  if snack: 
    db.session.add(snack)
    db.session.commit()
    return jsonify(data), 201
  
  return jsonify({'message': 'Dados inválidos!'}), 400

@app.route('/snack/<int:user_id>', methods=['PUT'])
def edit_snack(user_id: int): 
  data = request.json
  snack = Snack.query.get(user_id)

  if snack:
    snack.description = data.get('description')
    snack.timestamp = datetime.today().date()
    snack.diet = data.get('diet')
    db.session.commit()
    return jsonify({'message': 'Atualizado dados!'})
  
  return jsonify({'message': 'Refeição não encontrada'}), 404 

if __name__ == '__main__':
  app.run(debug=True)