from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

# 模拟用户数据库
mock_user_db = {
    'user1': 'password123',
    'user2': 'mypassword'
}

# 登录路由
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # 验证用户名和密码
    if mock_user_db.get(username) == password:
        # 如果验证成功，创建响应并设置 Cookie
        response = make_response(jsonify({'message': 'Login successful'}))
        response.set_cookie('username', username)
        return response
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

# 检查登录状态的路由
@app.route('/status', methods=['GET'])
def status():
    username = request.cookies.get('username')

    if username:
        return jsonify({'message': f'User {username} is logged in.'})
    else:
        return jsonify({'message': 'User is not logged in.'}), 401

# 登出路由
@app.route('/logout', methods=['POST'])
def logout():
    response = make_response(jsonify({'message': 'Logged out successfully'}))
    response.delete_cookie('username')
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
