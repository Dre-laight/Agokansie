from flask import Flask,request,jsonify
from flask_socketio import SocketIO,emit
from flask_cors import CORS

Active_Game=None
Games=["oware","dame","achi"]
app=Flask(__name__)
CORS(app)
socketio=SocketIO(app,cors_allowed_origins="*")
@app.route("/")
def home():
    return "drone"
@app.route("/game/select",methods=["POST"])
def game_type():
    global Games
    data=request.json
    Active_Game=data["game_choice"]
    
    print(Active_Game)
    return jsonify ({"message":"successfull"})
    # return "drone"
@socketio.on("game_state")
def handle_move(data):
    data={
        "board": [4,4,4,4,4,4,4,4,4,4,4,4],
        "hints":"bad move",
        
    }
    if Active_Game==Games[0]:
       emit("oware_board", {
            "game":"oware", 
            "turn":"robot",
            "board":[4,4,4,4,4,4,4,4,4,4,4,4]
        }, broadcast=True)
    elif Active_Game==Games[1]:
       emit("dame_board", {
            "board_state": data ,
            "message": "Move received"
        }, broadcast=True)
    elif Active_Game==Games[2]:
       emit("achi_board", {
            "board_state": data ,
            "message": "Move received"
        }, broadcast=True)
    

if __name__ =="__main__":
    socketio.run(app,
                host="0.0.0.0",
                port=5000,
                debug=False)