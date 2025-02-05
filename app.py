from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route('/api', methods=['GET'])
def get_info():
    response = {
        "email": "olamidefiyin18@gmail.com",  
        "current_datetime": datetime.utcnow().isoformat() + 'Z',
        "github_url": "https://github.com/Holarmitidey/HNG-Taskzero"
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)