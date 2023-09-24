from flask import Flask, render_template
import random

app = Flask(__name__)
move1 = ""
move2 = ""
move3 = ""
move4 = ""

Moves = ["chest level punch", "Face level punch", "Lower level punch", "Face level kick", "Chest level kick", "Lower level kick", "Round House kick", "upper Block", "Inner Block", "Outer Block", "Lower Block"]

@app.route("/")
def Index():
    return render_template("Index.html", Move1 = move1, Move2 = move2, Move3 = move3, Move4 = move4)

@app.route("/Randomize")
def Randomize():
    move1 = random.choice(Moves)
    move2 = random.choice(Moves)
    move3 = random.choice(Moves)
    move4 = random.choice(Moves)

    return render_template("Index.html", Move1 = move1, Move2 = move2, Move3 = move3, Move4 = move4)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
