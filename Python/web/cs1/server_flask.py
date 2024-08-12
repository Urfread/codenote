from flask import Flask, jsonify, request

app = Flask(__name__)

# 模拟一个简单的数据库
mock_db = {
    'msg': 'Hello World!'
}

# GET 请求：获取指定项目信息
@app.route('/process_request/<string:category>/<int:item_id>', methods=['GET'])
def process_request(category, item_id):
    # 模拟处理
    data = {
        'message': 'GET request received and processed successfully!',
        'category': category,
        'item_id': item_id,
        'info': f'You requested {category} with ID {item_id}',
        'data': mock_db.get(item_id, 'No data found for this ID.')
    }
    return jsonify(data)

# POST 请求：创建新项目
@app.route('/process_request/<string:category>', methods=['POST'])
def create_item(category):
    item_id = request.json.get('item_id')
    details = request.json.get('details')
    
    # 模拟在数据库中创建新项目
    mock_db[item_id] = {'category': category, 'details': details}
    
    data = {
        'message': 'POST request received and processed successfully!',
        'item_id': item_id,
        'category': category,
        'details': details
    }
    return jsonify(data)

# PUT 请求：更新现有项目
@app.route('/process_request/<string:category>/<int:item_id>', methods=['PUT'])
def update_item(category, item_id):
    if item_id in mock_db:
        details = request.json.get('details')
        
        # 模拟更新数据库中的项目
        mock_db[item_id]['details'] = details
        
        data = {
            'message': 'PUT request received and processed successfully!',
            'item_id': item_id,
            'category': category,
            'details': details
        }
    else:
        data = {
            'message': 'Item not found.',
            'item_id': item_id
        }
    return jsonify(data)

# DELETE 请求：删除现有项目
@app.route('/process_request/<string:category>/<int:item_id>', methods=['DELETE'])
def delete_item(category, item_id):
    if item_id in mock_db:
        # 模拟删除数据库中的项目
        del mock_db[item_id]
        data = {
            'message': 'DELETE request received and processed successfully!',
            'item_id': item_id,
            'category': category
        }
    else:
        data = {
            'message': 'Item not found.',
            'item_id': item_id
        }
    return jsonify(data)
# GET 请求：返回一个Hello World响应
@app.route('/practice_request',methods=['GET'])
def pactice_request():
    return jsonify({'message':mock_db['msg']})
# PUT 请求：更新 msg 的值
@app.route('/practice_request/updatemsg', methods=['PUT'])
def practice_updatemsg():
    # 从请求体中获取 msg
    msg = request.json.get('msg')
    
    # 更新 mock_db 中的 msg 值
    mock_db['msg'] = msg
    
    # 返回更新后的 msg
    return jsonify({'message': mock_db['msg']})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
