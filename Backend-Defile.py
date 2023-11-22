from flask import Flask, request, make_response, render_template, jsonify
from flask_cors import CORS
import copy
import os
from BackDefile.Minion import Minion
from BackDefile.Board import Board
from BackDefile.Owner_enum import owner
from BackDefile.Defile import Calculate

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return render_template("Defile.html")


@app.route("/process_data", methods=["GET", "POST"])
def process_data():
    # if request.method == 'OPTIONS':
    #     print("triggered")
    #     response = make_response()
    #     response.headers['Access-Control-Allow-Origin'] = request.headers.get('Origin', '*')
    #     response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    #     response.headers.add('Access-Control-Allow-Methods', 'GET, PUT, POST, DELETE, OPTIONS')
    #     return response
    frontend_defile = request.get_json()
    print(len(frontend_defile))
    board = Board()
    for index, obj in enumerate(frontend_defile, start=1):
        if obj["attack"] == "" or obj["health"] == "":
            continue
        attack = int(obj["attack"])
        health = int(obj["health"])
        taunt = obj["taunt"]
        ds = obj["ds"]
        reborn = obj["reborn"]
        if index >= 1 and index < 8:
            name = "E" + str(index)
            minion = Minion(attack, health, name, owner.enemy, taunt, ds, reborn)
        else:
            name = "F" + str(index - 7)
            minion = Minion(attack, health, name, owner.friendly, taunt, ds, reborn)
        board.add_minion(minion)

    process = Calculate()

    if board.check_termination() == False:
        process.activate_defile(copy.deepcopy(board))
        if process.solution == None:
            response = jsonify({"solution": "扭了扭了", "scenes": None})
            response.headers.add("Access-Control-Allow-Origin", "*")
            return response
        else:
            process.get_scenes(board)
            print(process.scenes)
            response = jsonify(
                {
                    "solution_list": process.solution,
                    "solution": "  ------->  ".join(process.solution),
                    "scenes": process.scenes,
                }
            )
            return response
    else:
        response = jsonify({"solution": "Good for Defile", "scenes": None})
        return response
from flask import redirect
@app.route('/https://defilecalculator-5d48601430ba.herokuapp.com/')
def index():
    return redirect("https://www.defilecalculator.com/", code=301)



if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
