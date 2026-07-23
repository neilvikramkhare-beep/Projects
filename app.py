from flask import Flask, redirect, render_template, request, session, url_for

from bank_state import apply_action, initial_state

app = Flask(__name__)
app.secret_key = "bank-app-secret"


def get_state():
    if "bank_state" not in session:
        session["bank_state"] = initial_state()
    return session["bank_state"]


@app.route("/", methods=["GET"])
def index():
    state = get_state()
    return render_template("index.html", state=state)


@app.route("/deposit", methods=["POST"])
def deposit():
    amount = request.form.get("amount", "0")
    state = get_state()
    state = apply_action(state, {"type": "DEPOSIT", "payload": amount})
    session["bank_state"] = state
    return redirect(url_for("index"))


@app.route("/withdraw", methods=["POST"])
def withdraw():
    amount = request.form.get("amount", "0")
    state = get_state()
    state = apply_action(state, {"type": "WITHDRAW", "payload": amount})
    session["bank_state"] = state
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
