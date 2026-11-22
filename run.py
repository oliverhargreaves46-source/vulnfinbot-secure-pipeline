from flask import Flask
from app.routes import bp

app = Flask(name)
app.register_blueprint(bp)

if name == 'main':
    app.run(host='0.0.0.0', port=5000)