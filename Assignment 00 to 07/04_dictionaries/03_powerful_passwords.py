# Task 3
# You want to be safe online and use different passwords for different websites. However, you are forgetful at times and want to make a program that can match which password belongs to which website without storing the actual password!

from hashlib import sha256

def hash_password(password):
    return sha256(password.encode()).hexdigest()

def login(email, store_login, password):
    return store_login.get(email) == hash_password(password)

def main():
    store_login = {
        "wallmart@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "web_developer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",
        "oepschool.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"
    }
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if email not in store_login:
        print("❌ Email not found.")
    elif login(store_login, password):
        print("✅ Login successful! Welcome!")
    else:
        print("❌ Invalid email or password. Please try again.")

if __name__ == '__main__':
    main()