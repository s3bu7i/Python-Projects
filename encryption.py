import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from getpass import getpass

# Generate encryption key using password-based key derivation function
def generate_key(password):
    salt = b'salt_'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key

# Encrypt data using Fernet encryption
def encrypt_data(key, data):
    f = Fernet(key)
    encrypted_data = f.encrypt(data.encode())
    return encrypted_data

# Decrypt data using Fernet encryption
def decrypt_data(key, encrypted_data):
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)
    return decrypted_data.decode()

# Main menu
def main_menu():
    print("Welcome to the Encryption Program!")
    print("1. Encrypt data")
    print("2. Decrypt data")
    print("3. Exit")

# Encrypt data submenu
def encrypt_submenu():
    print("\nEncrypt data using:")
    print("1. Base64")
    print("2. Fernet")
    print("3. Return to main menu")

# Decrypt data submenu
def decrypt_submenu():
    print("\nDecrypt data using:")
    print("1. Base64")
    print("2. Fernet")
    print("3. Return to main menu")

# User interface
def user_interface():
    while True:
        main_menu()
        choice = input("\nEnter your choice: ")

        if choice == '1':
            encrypt_submenu()
            encrypt_choice = input("Enter your choice: ")

            if encrypt_choice == '1':
                data = input("Enter the data to encrypt: ")
                encrypted_data = base64.b64encode(data.encode()).decode()
                print("Encrypted data:", encrypted_data)

            elif encrypt_choice == '2':
                data = input("Enter the data to encrypt: ")
                password = getpass("Enter the encryption password: ")
                key = generate_key(password.encode())
                encrypted_data = encrypt_data(key, data)
                print("Encrypted data:", encrypted_data.decode())

            elif encrypt_choice == '3':
                continue

            else:
                print("Invalid choice. Please try again.")

        elif choice == '2':
            decrypt_submenu()
            decrypt_choice = input("Enter your choice: ")

            if decrypt_choice == '1':
                encrypted_data = input("Enter the data to decrypt: ")
                decrypted_data = base64.b64decode(encrypted_data.encode()).decode()
                print("Decrypted data:", decrypted_data)

            elif decrypt_choice == '2':
                encrypted_data = input("Enter the data to decrypt: ")
                password = getpass("Enter the encryption password: ")
                key = generate_key(password.encode())
                decrypted_data = decrypt_data(key, encrypted_data.encode())
                print("Decrypted data:", decrypted_data)

            elif decrypt_choice == '3':
                continue

            else:
                print("Invalid choice. Please try again.")

        elif choice == '3':
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == '__main__':
    user_interface()
