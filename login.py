# # login.py
# import streamlit as st
# import hashlib
# import sqlite3

# # Database setup
# def create_user_table():
#     conn = sqlite3.connect('users.db')
#     c = conn.cursor()
#     c.execute('CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT)')
#     conn.commit()
#     conn.close()

# def add_user(username, password):
#     conn = sqlite3.connect('users.db')
#     c = conn.cursor()
#     c.execute('INSERT INTO users(username, password) VALUES (?, ?)', (username, password))
#     conn.commit()
#     conn.close()

# def check_user(username, password):
#     conn = sqlite3.connect('users.db')
#     c = conn.cursor()
#     c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
#     data = c.fetchone()
#     conn.close()
#     return data

# # Password hashing
# def hash_password(password):
#     return hashlib.sha256(str.encode(password)).hexdigest()

# # Login function
# def login():
#     st.title("Login")
#     username = st.text_input("Username")
#     password = st.text_input("Password", type='password')
#     hashed_password = hash_password(password)

#     if st.button("Login"):
#         user = check_user(username, hashed_password)
#         if user:
#             st.success("Logged in successfully!")
#             st.session_state['logged_in'] = True
#             st.session_state['username'] = username
#             return True  # Login successful
#         else:
#             st.error("Invalid username or password")
#             return False

# # Registration function
# def register():
#     st.title("Register")
#     new_user = st.text_input("Username")
#     new_password = st.text_input("Password", type='password')
#     hashed_password = hash_password(new_password)

#     if st.button("Register"):
#         create_user_table()
#         add_user(new_user, hashed_password)
#         st.success("Registration successful! You can now log in.")

# # Logout function
# def logout():
#     st.session_state['logged_in'] = False
#     st.success("You have been logged out.")
