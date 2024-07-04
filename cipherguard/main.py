from flask import Flask, render_template, request, jsonify
from cipherguard.encryption import encrypt_message, decrypt_message, encrypt_file, decrypt_file
from cipherguard.key_management import generate_key, store_key, retrieve_key

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    message = data['message']
    algorithm = data['algorithm']
    key = generate_key(algorithm)
    store_key(key, algorithm)
    encrypted = encrypt_message(message, key, algorithm)
    return jsonify({'encrypted': encrypted, 'key': key})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    encrypted = data['encrypted']
    algorithm = data['algorithm']
    key = data['key']
    decrypted = decrypt_message(encrypted, key, algorithm)
    return jsonify({'decrypted': decrypted})

@app.route('/encrypt_file', methods=['POST'])
def encrypt_file_route():
    file = request.files['file']
    algorithm = request.form['algorithm']
    key = generate_key(algorithm)
    store_key(key, algorithm)
    encrypted_file = encrypt_file(file, key, algorithm)
    return jsonify({'encrypted_file': encrypted_file, 'key': key})

@app.route('/decrypt_file', methods=['POST'])
def decrypt_file_route():
    file = request.files['file']
    algorithm = request.form['algorithm']
    key = request.form['key']
    decrypted_file = decrypt_file(file, key, algorithm)
    return jsonify({'decrypted_file': decrypted_file})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
else:
    application = app