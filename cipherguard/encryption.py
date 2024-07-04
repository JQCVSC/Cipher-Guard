from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

def encrypt_message(message, key, algorithm):
    if algorithm == 'AES':
        f = Fernet(key)
        return f.encrypt(message.encode()).decode()
    elif algorithm == 'RSA':
        public_key = serialization.load_pem_public_key(key.encode())
        encrypted = public_key.encrypt(
            message.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted.hex()

def decrypt_message(encrypted, key, algorithm):
    if algorithm == 'AES':
        f = Fernet(key)
        return f.decrypt(encrypted.encode()).decode()
    elif algorithm == 'RSA':
        private_key = serialization.load_pem_private_key(key.encode(), password=None)
        decrypted = private_key.decrypt(
            bytes.fromhex(encrypted),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted.decode()

def encrypt_file(file, key, algorithm):
    # Implement file encryption logic here
    pass

def decrypt_file(file, key, algorithm):
    # Implement file decryption logic here
    pass