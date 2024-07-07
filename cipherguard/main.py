from flask import Flask, render_template, request, jsonify
from app.encryption import encrypt_message, decrypt_message, generate_rsa_keys
from app.key_management import generate_key, store_key, retrieve_key

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    message = data['message']
    algorithm = data['algorithm']
    if algorithm == 'RSA':
        private_key, public_key = generate_rsa_keys()
        encrypted = encrypt_message(message, public_key, algorithm)
        return jsonify({'encrypted': encrypted, 'key': private_key})
    else:  # AES
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)