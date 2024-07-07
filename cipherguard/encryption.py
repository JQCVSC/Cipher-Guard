from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.fernet import Fernet
import base64

def generate_rsa_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    
    return private_pem.decode(), public_pem.decode()

def encrypt_message(message, key, algorithm):
    if algorithm == 'AES':
        f = Fernet(key.encode())
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
        return base64.b64encode(encrypted).decode()

def decrypt_message(encrypted, key, algorithm):
    if algorithm == 'AES':
        f = Fernet(key.encode())
        return f.decrypt(encrypted.encode()).decode()
    elif algorithm == 'RSA':
        private_key = serialization.load_pem_private_key(key.encode(), password=None)
        decrypted = private_key.decrypt(
            base64.b64decode(encrypted),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted.decode()