# app.py
from flask import Flask, request, jsonify, render_template_string, send_file
import jwt
import sqlite3
import logging
import os
from datetime import datetime
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key-123'
app.config['UPLOAD_FOLDER'] = 'uploads'

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
    filename='app.log'
)

def get_db():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/init')
def init_db():
    conn = get_db()
    conn.execute('''CREATE TABLE IF NOT EXISTS users 
                    (id INTEGER PRIMARY KEY, username TEXT, password TEXT, role TEXT)''')
    conn.execute('''INSERT OR IGNORE INTO users (username, password, role) 
                    VALUES ('admin', 'admin123', 'admin')''')
    conn.commit()
    return "DB initialized"

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    conn = get_db()
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    user = conn.execute(query).fetchone()

    if user:
        token = jwt.encode(
            {'user': username, 'role': user['role']}, 
            app.config['SECRET_KEY'], 
            algorithm='HS256'
        )
        return jsonify({"token": token})
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/users')
def list_users():
    conn = get_db()
    users = conn.execute('SELECT username, role FROM users').fetchall()
    return jsonify([dict(user) for user in users])

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file uploaded', 400

    file = request.files['file']
    if file.filename == '':
        return 'No file selected', 400

    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return 'File uploaded successfully'

@app.route('/files/<path:filename>')
def download_file(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename))

@app.route('/template')
def custom_template():
    template = request.args.get('template', '{{message}}')
    return render_template_string(template, message="Welcome!")

@app.route('/export')
def export_data():
    data = {
        'system_info': {
            'python_version': os.sys.version,
            'platform': os.sys.platform,
            'path': os.sys.path,
        },
        'environment': dict(os.environ),
        'app_config': {
            'secret_key': app.config['SECRET_KEY'],
            'debug': app.debug,
        }
    }
    return jsonify(data)

@app.route('/logs')
def view_logs():
    try:
        with open('app.log', 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "No logs found"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
