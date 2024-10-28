import socket
from DES_CBC import des_cbc_decrypt_base64, des_cbc_encrypt_base64  

def server_program():
    host = socket.gethostname()
    port = 5000  

    server_socket = socket.socket()  
    server_socket.bind((host, port))  

    server_socket.listen(2)
    conn, address = server_socket.accept()  
    print("Connection from: " + str(address))

    key = "mysecret"  
    iv = "initvect"   

    while True:
        
        data = conn.recv(1024).decode()
        if not data:
            
            break

        print("Received from client (encrypted): " + data)
        
        
        decrypted_message = des_cbc_decrypt_base64(data, key, iv)
        print("Decrypted message from client:", decrypted_message)

        
        response = input("Enter response -> ")
        encrypted_response = des_cbc_encrypt_base64(response, key, iv)
        conn.send(encrypted_response.encode())  

    conn.close()  


if __name__ == '__main__':
    server_program()
