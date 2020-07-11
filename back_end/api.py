import flask
from flask import request, jsonify
from flask_cors import CORS
import json

app = flask.Flask('search')
app.config["DEBUG"] = True
CORS(app)
with open('words_dictionary.json','r') as fp:
    data = json.load(fp).keys()

@app.route('/api/v1/search', methods=['GET'])
def list_similar_words():
    param = request.args['param']
    result = []
    count = 0
    for res in data:
        if res.startswith(param):
            result.append(res)
            count += 1
        if count == 1000:
            break

    return {
        "body": result
    }

app.run()