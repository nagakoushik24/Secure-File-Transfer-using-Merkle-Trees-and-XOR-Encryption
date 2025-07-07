# 🔐 Secure File Transfer using Merkle Trees and XOR Encryption

## 📌 Overview

This project demonstrates a **client-server file transfer system** implemented in Python using **socket programming**, **XOR encryption**, and **Merkle tree-based data integrity verification**. It incorporates core **Data Structures and Algorithms (DSA)** concepts such as **chunking**, **binary tree hashing (Merkle Trees)**, and **custom symmetric encryption**, making it a strong academic and portfolio project.

---

## 🧠 Key Concepts Used

- 📦 **File Chunking**: Divides large files into 1024-byte blocks for transmission.
- 🌳 **Merkle Tree Construction**: Builds a hash-based binary tree to verify file integrity using `hashlib.sha256`.
- 🔐 **Symmetric Encryption (XOR)**: Applies a custom byte-wise XOR encryption using a pseudo-random key.
- 🔗 **Socket Programming (TCP)**: Establishes reliable two-way communication between client and server.

---

## 🛠️ Tech Stack

- **Language**: Python 3
- **Libraries**: `socket`, `hashlib`, `os`, `secrets`
- **Encryption Logic**: XOR-based (with rotating key index)
- **DSA Logic**: Merkle Tree, File Chunking, Hash Trees

---

## 📁 Folder Structure
```
secure_file_transfer/
├── client.py # Sends encrypted file, key, and Merkle root
├── server.py # Receives file, decrypts, and verifies integrity
├── msg.txt # File to be sent
├── rsv_msg.txt # Output file (received + verified)
└── README.md # Project documentation
```


---

## 🧩 How It Works

### 🔁 Client Side (`client.py`)
1. Reads `msg.txt` as raw bytes.
2. Generates a random 32-byte key and encrypts file contents using XOR.
3. Splits the encrypted file into 1024-byte chunks.
4. Constructs a **Merkle Tree** (binary hash tree) using SHA-256.
5. Sends the following to the server via socket:
   - Encrypted chunks
   - XOR key
   - Merkle root hash

---

### 🧷 Server Side (`server.py`)
1. Receives:
   - Encrypted file chunks
   - Key
   - Merkle root
2. Decrypts the data using the XOR key.
3. Regenerates Merkle root hash from received chunks.
4. Compares computed root with received root.
5. If matched, writes the file to `rsv_msg.txt` and confirms successful integrity verification.

---

## 🧪 Sample Console Output
```
File Content Before Encryption: b'Hello World'
Encrypted File: b'\x1a\x0b...'
Merkle Root: a97c54f2ef3f...
File received and verified successfully.
```


---

## ✅ Features

- 🔐 Secure file transfer using XOR symmetric encryption
- 🌳 Verifiable integrity using Merkle root comparison
- 🔗 Reliable data transmission over TCP sockets
- 🧠 Educational and modular implementation for learning DSA, Networking, and Cryptography

---

## 📚 Learning Outcomes

- Implementing **Merkle Trees** for data verification
- Understanding **socket-level TCP/IP communication**
- Designing **custom symmetric encryption**
- Applying **chunk-based file handling** for secure transfer
- Bridging **DSA + Systems + Security**

---

## 🌍 Applications

- ✅ **Educational Tools** for teaching hashing, encryption, and networks
- 🧾 **Secure Log Transmission** across distributed systems
- 🔐 **Blockchain Prototypes** (Merkle trees are the basis of blockchain integrity)
- 🧠 **Cryptographic Protocol Demos** for verifying tamper-proof data exchange
- 📁 **Secure File Storage** in peer-to-peer systems with integrity verification

---

## 🧠 Future Enhancements

- 👥 Add **multi-client support** using threading or async sockets
- 🔐 Replace XOR with **AES or RSA** for real-world encryption
- 🌳 Send full **Merkle path proof** for partial file verification
- 🚨 Implement **hash mismatch reporting and alerts**
- 🗃️ Compress file chunks before transfer for optimization

---




