import socket
import hashlib

def generate_merkle_tree(file_chunks):
    hash_list = [hashlib.sha256(block).hexdigest() for block in file_chunks]

    while len(hash_list) > 1:
        hash_list = [hashlib.sha256((hash_list[i] + hash_list[i + 1]).encode('utf-8')).hexdigest() for i in range(0, len(hash_list), 2)]
    hash_list = [hash_list[0].encode()]
    return hash_list

def decrypt(encrypted_data, key):
    decrypted_data = bytearray()
    key_index = 0
    for byte in encrypted_data:
        decrypted_byte = byte ^ key[key_index % len(key)]
        decrypted_data.append(decrypted_byte)
        key_index += 1
    return bytes(decrypted_data)

def receive_file_and_verify(client_socket):
    encrypted_file = client_socket.recv(4096)
    key = client_socket.recv(32)
    print(encrypted_file)
    # Receive Merkle tree data in chunks
    merkle_tree_chunks = []
    while True:
        chunk = client_socket.recv(4096)
        if not chunk:
            break
        merkle_tree_chunks.append(chunk)
    # Concatenate the Merkle tree data
    file_list = [encrypted_file]
    # Rest of the code remains unchanged...

    decrypted_file = decrypt(encrypted_file, key)
    received_merkle_tree = generate_merkle_tree(file_list)

    print("Received Merkle Tree:", received_merkle_tree)
    print("Decrypted File Content:", decrypted_file)
    print("Received Merkle Tree Chunk:", merkle_tree_chunks)
    received_merkle = received_merkle_tree
    print(received_merkle)
    if received_merkle == merkle_tree_chunks:
        return decrypted_file
    else:
        return None

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.59.248', 5555))
    server_socket.listen(1)
    print("Server is listening for incoming connections...")
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")
    # Receive and verify the file
    verified_file = receive_file_and_verify(client_socket)
    if verified_file:
        with open("rsv_msg.txt", "wb") as f:
            f.write(verified_file)
            print("File received and verified successfully.")
    else:
        print("File integrity verification failed.")
    server_socket.close()

if __name__ == '__main__':
    main()