import mysql.connector
from mysql.connector import Error

# 数据库连接配置
config = {
    'user': 'root',
    'password': '123456',
    'host': '127.0.0.1',
    'database': 'mine2024'
}

def insert_data(cursor):
    try:
        # 插入模拟数据
        insert_query = """
        INSERT INTO evo_note (note_id, uid, question, answer)
        VALUES (%s, %s, %s, %s)
        """
        data = [
            ('note1', 'user1', 'What is Python?', 'A programming language.'),
            ('note2', 'user1', 'What is SQL?', 'A query language for databases.'),
            ('note3', 'user2', 'What is Flask?', 'A web framework for Python.')
        ]
        cursor.executemany(insert_query, data)
        print(f"{cursor.rowcount} rows inserted.")
    except Error as e:
        print(f"Error inserting data: {e}")

def query_data(cursor):
    try:
        # 查询数据
        query = "SELECT * FROM evo_note"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(f"Error querying data: {e}")

def update_proficiency(cursor,note_id,proficiency):
    try:
        # 更新笔记的熟练度
        update_query = """
        UPDATE evo_note
        SET proficiency = %s
        WHERE note_id = %s
        """
        cursor.execute(update_query, (proficiency, note_id))
        print(f"{cursor.rowcount} rows updated.")
    except Error as e:
        print(f"Error updating data: {e}")
def main():
    try:
        # 连接到 MySQL 数据库
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            cursor = connection.cursor()

            # # 插入数据
            # insert_data(cursor)
            # connection.commit()  # 提交事务

            # # 查询数据
            # query_data(cursor)

            # 更新熟练度
            update_proficiency(cursor, 'note1', 1)
            connection.commit()
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    main()
