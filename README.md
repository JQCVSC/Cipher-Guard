<<<<<<< HEAD
CipherGuard is a web-based encryption and decryption tool that supports multiple algorithms including AES and RSA.

## Features

- Message encryption and decryption
- File encryption and decryption
- Support for AES and RSA algorithms
- User-friendly web interface

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python app/main.py`

## Docker Setup

1. Build the Docker image: `docker build -t cipherguard .`
2. Run the container: `docker run -p 8080:8080 cipherguard`

## Running Tests

Run the tests using the following command:
python -m unittest discover tests
Copy
## Security Considerations

This tool is for educational purposes. For production use, ensure proper key management and consider additional security measures.
This project provides a basic framework for an encryption/decryption tool with a web interface. It supports both AES and RSA algorithms for message encryption and decryption. The file encryption/decryption functionality is left as a placeholder for you to implement.
Remember to handle keys securely in a real-world application. The key management functions (store_key and retrieve_key) are placeholders where you'd implement secure key storage and retrieval mechanisms.
You can expand on this project by adding more encryption algorithms, implementing the file encryption/decryption functions, improving the user interface, and enhancing overall security measures
=======
# Cipher-Guard
>>>>>>> 8aae9544553cbd49e9c0610fb6a3af139c3e167c
