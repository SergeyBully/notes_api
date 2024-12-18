from flask import Flask, jsonify
import logging
from app.api.endpoints.notes import notes_bp
from app.api.endpoints.types import types_bp
from app.api.endpoints.update_history import update_history_bp
from app.api.db.initialize_types import initialize_types


app = Flask(__name__)
logger = logging.getLogger(__name__)


app.register_blueprint(notes_bp)
app.register_blueprint(types_bp)
app.register_blueprint(update_history_bp)


@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask API!"})

if __name__ == '__main__':
    logger.info("Starting server...")
    app.run(host='0.0.0.0', port=5000, debug=True)
    initialize_types()
