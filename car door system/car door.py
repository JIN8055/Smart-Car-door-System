from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Mock data for car lock status
car_status = {
    "car_id": "123ABC",
    "is_locked": True,
    "battery_level": 80
}

@app.route('/lock', methods=['POST'])
def lock_car():
    car_status['is_locked'] = True
    return jsonify({"status": "locked", "timestamp": datetime.now()}), 200

@app.route('/unlock', methods=['POST'])
def unlock_car():
    car_status['is_locked'] = False
    return jsonify({"status": "unlocked", "timestamp": datetime.now()}), 200

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify(car_status), 200

if __name__ == '__main__':
    app.run(debug=True)
