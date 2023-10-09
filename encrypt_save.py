from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from pathlib import Path

# Load the recipient's public key from a file
def load_public_key_from_file(public_key_file_path):
    with open(public_key_file_path, "rb") as public_key_file:
        public_key = serialization.load_pem_public_key(
            public_key_file.read(),
            backend=default_backend()
        )
    return public_key

# Encrypt content using the recipient's public key and save to a file
def encrypt_and_save(content, public_key, output_file_path):
    ciphertext = public_key.encrypt(
        content.encode("utf-8"),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    with open(output_file_path, "wb") as encrypted_file:
        encrypted_file.write(ciphertext)

# Example usage:

root = Path().cwd() 

file_name = input("Write the file name: ")
recipient_public_key_file = Path().joinpath(root, "encryption/keys/public_key.pem")
output_encrypted_file = Path().joinpath(root, f"encryption/encrypted/{file_name}.bin")
file_path =Path().joinpath(root, f"encryption/files/{file_name}.txt") 
with open(file_path, mode='r', encoding="utf-8") as f:
    plaintext_content = f.read()

recipient_public_key = load_public_key_from_file(recipient_public_key_file)
encrypt_and_save(plaintext_content, recipient_public_key, output_encrypted_file)
