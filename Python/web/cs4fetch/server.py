from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许所有来源的跨域请求

# 模拟用户数据库
mock_user_db = {
    "title": "Welcome to My Site",
    "description": "This is a simple example of using fetch to load JSON data.",
    "items": [
        "Item 1",
        "Item 2",
        "Item 3"
    ]
}

# 获取数据的路由
@app.route('/getdata', methods=['GET'])
def get_data():
    return jsonify(mock_user_db)

# 修改数据的路由
@app.route('/updatedata', methods=['POST'])
def update_data():
    new_data = request.json
    if new_data:
        mock_user_db.update(new_data)
        return jsonify({"message": "Data updated successfully", "data": mock_user_db}), 200
    else:
        return jsonify({"message": "No data provided"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
