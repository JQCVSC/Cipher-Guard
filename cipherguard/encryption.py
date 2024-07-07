from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import base64

def generate_rsa_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
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

def rsa_encrypt(message, public_key):
    public_key = serialization.load_pem_public_key(public_key.encode(), backend=default_backend())
    encrypted = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return base64.b64encode(encrypted).decode()

def rsa_decrypt(encrypted, private_key):
    try:
        private_key = serialization.load_pem_private_key(
            private_key.encode(),
            password=None,
            backend=default_backend()
        )
        decrypted = private_key.decrypt(
            base64.b64decode(encrypted),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted.decode()
    except ValueError as e:
        print(f"Decryption error: {str(e)}")
        raise ValueError("Invalid key format or encrypted data")

def aes_encrypt(message, key):
    f = Fernet(key)
    return f.encrypt(message.encode()).decode()

def aes_decrypt(encrypted, key):
    f = Fernet(key)
    return f.decrypt(encrypted.encode()).decode()

def encrypt_message(message, key, algorithm):
    if algorithm == 'AES':
        return aes_encrypt(message, key)
    elif algorithm == 'RSA':
        return rsa_encrypt(message, key)
    else:
        raise ValueError("Unsupported algorithm")

def decrypt_message(encrypted, key, algorithm):
    if algorithm == 'AES':
        return aes_decrypt(encrypted, key)
    elif algorithm == 'RSA':
        return rsa_decrypt(encrypted, key)
    else:
        raise ValueError("Unsupported algorithm")