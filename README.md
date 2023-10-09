# Python Encryption App with `cryptography` 🐍🔒

This Python application provides a user-friendly way to encrypt and decrypt files using asymmetric encryption with public and private keys. It uses the `cryptography` library for encryption and decryption operations. The project follows a specific file structure to manage encrypted and decrypted files. 📁🔐

## Project Structure 📂

The project has the following directory structure:

- `encryption` (folder where decrypted files are saved) 📁
  - `decrypted` (decrypted files) 📁🔓
  - `encrypted` (encrypted files) 📁🔒
  - `files` (folder for files you want to encrypt) 📁📄
  - `keys` (folder for storing public and private keys) 📁🔑

## Getting Started 🚀

Before using the encryption and decryption features, you need to create your public and private keys using the `create_keys.py` module. Run the following command to generate keys:

```bash
python create_keys.py 🛡️

This will generate public_key.pem and private_key.pem files in the keys folder.

## Encrypting Files 🔐

You can encrypt files located in the files folder using the encrypt_save.py module. To encrypt a file, use the following command:

```bash
  python encrypt_save.py <filename> 📁🔒

Replace <filename> to encrypt with the name of the file you want to encrypt. The encrypted file will be saved in the encryption/encrypted folder.

## Decrypting Files 🔓

To decrypt files that are located in the encryption/encrypted folder, use the decrypt_save.py module. Run the following command:

```bash
  python decrypt_save.py <encrypted_filename> 🔓

Replace <encrypted_filename> with the name of the encrypted file you want to decrypt. The decrypted file will be saved in the encryption/decrypted folder.

## Note 📝

Make sure to keep your private key (private_key.pem) safe and never share it with others. 🤐🔐
You can encrypt multiple files, and each encrypted file will have its corresponding decrypted version.
You can customize the files in the files folder or add your own files for encryption. 🧾📂
Enjoy secure file encryption and decryption with this Python application! 🎉🔐📂