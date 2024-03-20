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
  description = data.get('description')
  diet = data.get('diet')

  snack = Snack(name=name, description=description, timestamp=datetime.today().date(), diet=diet)

  if snack: 
    db.session.add(snack)
    db.session.commit()
    return jsonify(data)
  
  return 'Error on server', 500

if __name__ == '__main__':
  app.run(debug=True)