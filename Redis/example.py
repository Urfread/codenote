import redis

# 连接到 Redis 服务器（包括密码）
r = redis.Redis(host='192.168.0.113', port=6379, db=0, password='123456')

# 设置一个键值对
r.set('username', 'Alice')

# 获取并打印键的值
username = r.get('username')
print(f'username: {username.decode("utf-8")}')

# 关闭连接
r.close()
