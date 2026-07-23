from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
patients = []
@app.route('/add', methods=['POST'])
def add_patient():
    data = request.json
    patients.append(data)
    return jsonify({"message": "Patient added successfully"})
@app.route('/patients', methods=['GET'])
def get_patients():
    return jsonify(patients)
@app.route('/search/<name>', methods=['GET'])
def search_patient(name):
    result = [p for p in patients if p['name'].lower() == name.lower()]
    return jsonify(result)
@app.route('/update', methods=['PUT'])
def update_payment():
    data = request.json
    name = data.get('name')
    new_payment = data.get('payment')
    for p in patients:
        if p['name'].lower() == name.lower():
            p['payment'] = new_payment
            return jsonify({"message": "Payment updated"})
    return jsonify({"message": "Patient not found"}), 404
@app.route('/delete/<name>', methods=['DELETE'])
def delete_patient(name):
    global patients
    patients = [p for p in patients if p['name'].lower() != name.lower()]
    return jsonify({"message": "Patient deleted"})
@app.route('/sort', methods=['GET'])
def sort_by_payment():
    sorted_data = sorted(patients, key=lambda x: x.get('payment', 0))
    return jsonify(sorted_data)
if __name__ == '__main__':
    app.run(debug=True)