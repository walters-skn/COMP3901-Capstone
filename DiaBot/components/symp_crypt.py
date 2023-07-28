from cryptography.fernet import fernet

def generate_key():
    return Fernet.generate_key()

def initialize_fernet(key):
    return Fernet(key)

def encrypt_data(fernet, data):
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

def decrypt_data(fernet, encrypted_data):
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    return decrypted_data