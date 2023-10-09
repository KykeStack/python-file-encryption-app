from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend
from pathlib import Path

# Load the recipient's private key from a file
def load_private_key_from_file(private_key_file_path):
    with open(private_key_file_path, "rb") as private_key_file:
        private_key = serialization.load_pem_private_key(
            private_key_file.read(),
            password=None,
            backend=default_backend()
        )
    return private_key

# Decrypt content using the recipient's private key and save to a file
def decrypt_and_save(encrypted_content_file_path, private_key, output_file_path):
    with open(encrypted_content_file_path, "rb") as encrypted_file:
        ciphertext = encrypted_file.read()
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    with open(output_file_path, "wb") as decrypted_file:
        decrypted_file.write(plaintext)

root = Path().cwd() 
# Example usage:
file_name = input("Write the file name: ")
recipient_private_key_file = Path().joinpath(root, "encryption/keys/private_key.pem")
input_encrypted_file = Path().joinpath(root, f"encryption/encrypted/{file_name}.bin")
output_decrypted_file =Path().joinpath(root, f"encryption/decrypted/decrypted_{file_name}.txt")

recipient_private_key = load_private_key_from_file(recipient_private_key_file)

decrypt_and_save(input_encrypted_file, recipient_private_key, output_decrypted_file)
