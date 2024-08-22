from flask import Flask
from config import Config
from models import db
from routes import api_blueprint

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database with the app context
with app.app_context():
    db.init_app(app)
    db.create_all()  # Create tables based on models

# Register API routes
app.register_blueprint(api_blueprint, url_prefix='/api')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
