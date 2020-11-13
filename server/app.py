"""
Flask Application for Plants

This hosts API routes & backend services. 
"""

import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS


PLANTS = [
    {
        'id': uuid.uuid4().hex,
        'name': 'Snake Boiii',
        'numPictures': '1',
        'picture': "https://www.pngitem.com/pimgs/m/516-5162680_snake-plant-png-transparent-png.png"
    },
    {
        'id': uuid.uuid4().hex,
        'name': 'Hole Boiii',
        'numPictures': '1',
        'picture': "https://i.pinimg.com/originals/2a/ce/37/2ace3738c7da0872edbc8388b1110ab5.png"
    }
]

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

def remove_plant(plant_id):
    for plant in PLANTS:
        if plant['id'] == plant_id:
            PLANTS.remove(plant)
            return True
    return False


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/plants', methods=['GET', 'POST'])
def all_plants():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        PLANTS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Plant added!'
    else:
        response_object['plants'] = PLANTS
    return jsonify(response_object)


@app.route('/plants/<plant_id>', methods=['PUT', 'DELETE'])
def single_plant(plant_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_plant(plant_id)
        PLANTS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Plant updated!'
    if request.method == 'DELETE':
        remove_plant(plant_id)
        response_object['message'] = 'Plant removed!'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
