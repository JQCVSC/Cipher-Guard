import unittest
from app.encryption import encrypt_message, decrypt_message

class TestEncryption(unittest.TestCase):
    def test_aes_encryption_decryption(self):
        message = "Hello, World!"
        key = b'your-32-byte-key-goes-here!!!!!'
        encrypted = encrypt_message(message, key, 'AES')
        decrypted = decrypt_message(encrypted, key, 'AES')
        self.assertEqual(message, decrypted)

    def test_rsa_encryption_decryption(self):
        # Implement RSA encryption/decryption test
        pass

if __name__ == '__main__':
    unittest.main()