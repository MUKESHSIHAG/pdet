from app import app
from flask import request, jsonify

@app.route('/')
def index():
    return "Pdet api is working properly"

@app.route('/get_result', methods=['GET'])
def get_result():
    res = 'Healthy'
    if request.args.get("ax")==request.args.get("ay")==request.args.get("az"):
        res="Unhealthy"
    return {"result": res, "msg": "Success"}