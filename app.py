import json
import os
from flask import Flask, request, jsonify
import requests
import structlog
import settings
from transformers import pipeline

app = Flask(__name__)


nlp = pipeline('question-answering',model='YOUR MODEL PATH')

@app.route('/healthz', methods=['GET'], strict_slashes=False)
def healthz():
    return jsonify({'status': 200})

@app.route('/search', methods=['GET','POST'])
def search():
    request_data = request.get_json()
    question = request_data['question']
    context = request_data['context']
    answer = nlp({'question': question,'context': context})
    response = {'answer': answer}
    print(f'Response: {json.dumps(response)}')
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=settings.PORT, debug=settings.DEBUG)
