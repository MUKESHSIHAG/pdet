from app import app
from flask import request, jsonify

@app.route('/get-result', methods=['GET'])
def index():
    print(request.args.get("ax"),request.args.get("az"))
    res = 'Good posture'
    if request.args.get("ax")==request.args.get("ay")==request.args.get("az"):
        res="Bad posture"
    return {"result": res, "msg": "Success"}