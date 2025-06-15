from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Hero, Power, HeroPower
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return "Flask Superheroes API"

# GET /heroes
@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes])

# GET /heroes/:id
@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({'error': 'Hero not found'}), 404
    return jsonify(hero.to_dict_with_powers())

# GET /powers
@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers])

# GET /powers/:id
@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({'error': 'Power not found'}), 404
    return jsonify(power.to_dict())

# PATCH /powers/:id
@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({'error': 'Power not found'}), 404
    
    data = request.get_json()
    if not data or 'description' not in data:
        return jsonify({'errors': ['Description is required']}), 400
    
    try:
        power.description = data['description']
        db.session.commit()
        return jsonify(power.to_dict())
    except ValueError as e:
        return jsonify({'errors': [str(e)]}), 400

# POST /hero_powers
@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    
    if not data:
        return jsonify({'errors': ['Request body is required']}), 400
    
    required_fields = ['strength', 'power_id', 'hero_id']
    for field in required_fields:
        if field not in data:
            return jsonify({'errors': [f'{field} is required']}), 400
    
    # Check if hero and power exist
    hero = Hero.query.get(data['hero_id'])
    power = Power.query.get(data['power_id'])
    
    if not hero:
        return jsonify({'errors': ['Hero not found']}), 400
    if not power:
        return jsonify({'errors': ['Power not found']}), 400
    
    try:
        hero_power = HeroPower(
            strength=data['strength'],
            hero_id=data['hero_id'],
            power_id=data['power_id']
        )
        db.session.add(hero_power)
        db.session.commit()
        return jsonify(hero_power.to_dict_with_hero()), 201
    except ValueError as e:
        return jsonify({'errors': [str(e)]}), 400

if __name__ == '__main__':
    app.run(debug=True)