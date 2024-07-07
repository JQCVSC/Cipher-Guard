from flask import Flask, render_template, request, jsonify
from cipherguard.encryption import encrypt_message, decrypt_message, generate_rsa_keys
from cryptography.fernet import Fernet
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    message = data['message']
    algorithm = data['algorithm']
    app.logger.debug(f"Encrypting message with algorithm: {algorithm}")
    if algorithm == 'RSA':
        private_key, public_key = generate_rsa_keys()
        app.logger.debug("RSA keys generated")
        encrypted = encrypt_message(message, public_key, algorithm)
        app.logger.debug("Message encrypted with RSA")
        return jsonify({'encrypted': encrypted, 'key': private_key})
    else:  # AES
        key = Fernet.generate_key().decode()
        encrypted = encrypt_message(message, key, algorithm)
        app.logger.debug("Message encrypted with AES")
        return jsonify({'encrypted': encrypted, 'key': key})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    encrypted = data['encrypted']
    algorithm = data['algorithm']
    key = data['key']
    app.logger.debug(f"Decrypting message with algorithm: {algorithm}")
    try:
        decrypted = decrypt_message(encrypted, key, algorithm)
        app.logger.debug("Message decrypted successfully")
        return jsonify({'decrypted': decrypted})
    except Exception as e:
        app.logger.error(f"Decryption error: {str(e)}")
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)