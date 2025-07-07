import socket
import os
import hashlib

def divide_file_into_chunks(file_content, chunk_size=1024):
    return [file_content[i:i + chunk_size] for i in range(0, len(file_content), chunk_size)]

def generate_merkle_tree(file_chunks):
    hash_list = [hashlib.sha256(block).hexdigest() for block in file_chunks]
    while len(hash_list) > 1:
        hash_list = [hashlib.sha256((hash_list[i] + hash_list[i + 1]).encode('utf-8')).hexdigest() for i in range(0, len(hash_list), 2)]
    return hash_list[0]
import secrets

def generate_random_key(length=32):
    return secrets.token_hex(length // 2)

def encrypt(data, key):
    encrypted_data = bytearray()
    key_index = 0
    for byte in data:
        encrypted_byte = byte ^ key[key_index % len(key)]
        encrypted_data.append(encrypted_byte)
        key_index += 1
    return bytes(encrypted_data)


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(('192.168.59.248', 5555))
        file_path = "msg.txt"  # Replace with your file path
        # Read the file content
        with open(file_path, "rb") as f:
            file_content = f.read()
        print(file_content)
        # Generate key and iv for encryption
        key = os.urandom(32)
        iv = os.urandom(16)
        print(key)
        # Encrypt the file
        encrypted_file = encrypt(file_content, key)
        print(encrypted_file)
        # Divide the encrypted file into chunks
        file_chunks = divide_file_into_chunks(encrypted_file)
        print(file_chunks)
        # Send encrypted file chunks
        for chunk in file_chunks:
            client_socket.sendall(chunk)
            print(chunk)
        # Send key
        client_socket.sendall(key)
        # Generate Merkle tree from file chunks
        merkle_tree_data = generate_merkle_tree(file_chunks)
        print(merkle_tree_data)
        print(merkle_tree_data.encode())
        # Send Merkle tree data
        client_socket.sendall(merkle_tree_data.encode())
    finally:
        client_socket.close()

if __name__ == '__main__':
    main()