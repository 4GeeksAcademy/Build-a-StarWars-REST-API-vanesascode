"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Characters, Planets, Starships, Fav_Characters, Fav_Planets, Fav_Starships
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

################################################################################

# GET ALL USERS

@app.route('/user', methods=['GET'])
def handle_hello():
    users = User.query.all()

    if not users:
        return jsonify(message="No users found"), 404

    all_users = list(map(lambda x: x.serialize(), users))
    return jsonify(message="Users", users=all_users), 200

# GET ONE USER

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({'message': 'User not found'}), 404

    serialized_user = user.serialize()
    return jsonify({'user': serialized_user}), 200


#################################################################################


@app.route('/characters', methods=['GET'])
def get_characters():
    characters = Characters.query.all()
    all_characters = list(map(lambda x: x.serialize(), characters))
    return jsonify(message="Characters", characters=all_characters), 200


@app.route('/planets', methods=['GET'])
def get_planets():
    planets = Planets.query.all()
    all_characters = list(map(lambda x: x.serialize(), characters))
    return jsonify(message="Characters", characters=all_characters), 200

@app.route('/starhips', methods=['GET'])
def get_starhips():
    response_body = {
        "msg": "Starhips got"
    }
    return jsonify(response_body), 200

###############################################################################

@app.route('/fav_characters', methods=['GET'])
def get_favcharacters():
    response_body = {
        "msg": "Fav Characters got"
    }
    return jsonify(response_body), 200

@app.route('/fav_planets', methods=['GET'])
def get_favplanets():
    response_body = {
        "msg": "Fav Planets got"
    }
    return jsonify(response_body), 200

@app.route('/fav_starhips', methods=['GET'])
def get_favstarhips():
    response_body = {
        "msg": "Fav Starhips got"
    }
    return jsonify(response_body), 200

###############################################################################

@app.route('/user', methods=['POST'])
def add_new_user():
    request_body_user = request.get_json()

    new_user = User(email=request_body_user["email"], password=request_body_user["password"], is_active=request_body_user["is_active"])
    db.session.add(new_user)
    db.session.commit()

    return jsonify(request_body_user), 200

@app.route('/characters', methods=['POST'])
def add_new_character():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    # characters.append(request_body)
    # return jsonify(characters)

###############################################################################

@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({'message': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': f'User with ID {user_id} deleted successfully'}), 200

@app.route('/characters/<int:id>', methods=['DELETE'])
def delete_character():
    request_body = request.json
    print("This is the request to delete", request_body)
    # characters.append(request_body)
    # return jsonify(characters)

###############################################################################

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)


# pipenv run python src/app.py