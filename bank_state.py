from copy import deepcopy
from datetime import datetime


def initial_state():
    return {"balance": 0.0, "transactions": []}


def apply_action(state, action):
    state = deepcopy(state)

    if action["type"] == "DEPOSIT":
        amount = round(float(action["payload"]), 2)
        state["balance"] = round(state["balance"] + amount, 2)
        state["transactions"].append(
            {
                "id": datetime.now().strftime("%H%M%S%f"),
                "type": "DEPOSIT",
                "amount": amount,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
        )
        return state

    if action["type"] == "WITHDRAW":
        amount = round(float(action["payload"]), 2)
        if state["balance"] >= amount:
            state["balance"] = round(state["balance"] - amount, 2)
            state["transactions"].append(
                {
                    "id": datetime.now().strftime("%H%M%S%f"),
                    "type": "WITHDRAW",
                    "amount": amount,
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
            )
        return state

    return state
