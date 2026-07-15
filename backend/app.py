from flask import Flask
from flask_cors import CORS

from routes.game_routes import game_bp
# from services.robot_controller import RobotController

# robot_controller = RobotController("COM6", 115200)

app = Flask(__name__)

CORS(app)

# CORS(
#     app,
#     resources={r"/*": {"origins": "*"}},
#     allow_headers=["Content-Type", "Authorization"],
#     methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"]
# )
# CORS(app, resources={r"/api/*": {"origins": "*"}})
app.register_blueprint(game_bp, url_prefix="/api")

@app.route("/")
def home():
    return {
        "status": "running",
        "message": "Board Game Robot Server"
    }

if __name__ == "__main__":
    app.run(
    host="0.0.0.0",
    port=5000,
    debug=True
    # threaded=True
)