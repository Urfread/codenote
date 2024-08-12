import requests

# 定义 API 的基础 URL
BASE_URL = 'http://127.0.0.1:5000/process_request'

def get_item():
    category = input("Enter category: ")
    item_id = input("Enter item ID: ")
    url = f"{BASE_URL}/{category}/{item_id}"
    response = requests.get(url)
    print(response.json())

def create_item():
    category = input("Enter category: ")
    item_id = input("Enter item ID: ")
    details = input("Enter details: ")
    url = f"{BASE_URL}/{category}"
    data = {'item_id': int(item_id), 'details': details}
    response = requests.post(url, json=data)
    print(response.json())

def update_item():
    category = input("Enter category: ")
    item_id = input("Enter item ID: ")
    details = input("Enter new details: ")
    url = f"{BASE_URL}/{category}/{item_id}"
    data = {'details': details}
    response = requests.put(url, json=data)
    print(response.json())

def delete_item():
    category = input("Enter category: ")
    item_id = input("Enter item ID: ")
    url = f"{BASE_URL}/{category}/{item_id}"
    response = requests.delete(url)
    print(response.json())

def update_msg():
    msg = input("Enter message: ")
    
    # 构造请求的 URL 和 JSON 数据
    url = f"http://127.0.0.1:5000/practice_request/updatemsg"
    response = requests.put(url, json={'msg': msg})
    
    # 输出服务器返回的 JSON 响应
    print(response.json())
def menu():
    while True:
        print("\n--- API Testing Menu ---")
        print("1. GET item")
        print("2. POST create item")
        print("3. PUT update item")
        print("4. DELETE item")
        print("5. PUT msg")
        print("0. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            get_item()
        elif choice == '2':
            create_item()
        elif choice == '3':
            update_item()
        elif choice == '4':
            delete_item()
        elif choice == '5':
            update_msg()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    menu()
