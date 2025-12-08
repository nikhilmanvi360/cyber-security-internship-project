from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"

def generate_key():
    """Generates a key and saves it into a file."""
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    """Loads the key from the current directory named `secret.key`."""
    if not os.path.exists(KEY_FILE):
        return None
    return open(KEY_FILE, "rb").read()

def encrypt_text(text, key):
    """Encrypts text using the provided key."""
    f = Fernet(key)
    if isinstance(text, str):
        text = text.encode()
    return f.encrypt(text)

def decrypt_text(encrypted_data, key):
    """Decrypts encrypted data using the provided key."""
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)
    return decrypted_data.decode()
