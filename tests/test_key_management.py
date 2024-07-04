import unittest
from app.key_management import generate_key, store_key, retrieve_key

class TestKeyManagement(unittest.TestCase):
    def test_aes_key_generation(self):
        key = generate_key('AES')
        self.assertIsNotNone(key)
        self.assertEqual(len(key), 44)  # Base64 encoded 32-byte key

    def test_rsa_key_generation(self):
        key = generate_key('RSA')
        self.assertIsNotNone(key)
        self.assertIn('BEGIN PUBLIC KEY', key)

    def test_key_storage_and_retrieval(self):
        # Generate a test key
        test_key = generate_key('AES')
        
        # Store the key
        key_id = store_key(test_key, 'AES')
        self.assertIsNotNone(key_id)

        # Retrieve the key
        retrieved_key = retrieve_key(key_id, 'AES')
        self.assertEqual(test_key, retrieved_key)

if __name__ == '__main__':
    unittest.main()