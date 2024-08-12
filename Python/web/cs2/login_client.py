import requests

# Flask 服务器的基础 URL
BASE_URL = 'http://127.0.0.1:5000'

# 创建一个 Session 对象来处理 Cookies
session = requests.Session()

def login(username, password):
    url = f"{BASE_URL}/login"
    data = {
        'username': username,
        'password': password
    }
    response = session.post(url, json=data)
    print(response.json())

def check_status():
    url = f"{BASE_URL}/status"
    response = session.get(url)
    print(response.json())

def logout():
    url = f"{BASE_URL}/logout"
    response = session.post(url)
    print(response.json())

def menu():
    while True:
        print("\n--- User Login Test Menu ---")
        print("1. Login")
        print("2. Check Login Status")
        print("3. Logout")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            login(username, password)
        elif choice == '2':
            check_status()
        elif choice == '3':
            logout()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    menu()
