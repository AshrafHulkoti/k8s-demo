from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({
        "message": "Welcome to Sample API",
        "status": "success",
        "data": {
            "items": [
                {"id": 1, "name": "Item 1"},
                {"id": 2, "name": "Item 2"},
                {"id": 3, "name": "Item 3"}
            ]
        }
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "message": "Resource not found",
        "status": "error",
        "error": str(error)
    }), 404

if __name__ == '__main__':
    # Run on port 80
    port = int(os.environ.get('PORT', 80))
    # Note: Running on port 80 requires root privileges
    app.run(host='0.0.0.0', port=port)
