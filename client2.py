import socket
from DES_CBC import des_cbc_encrypt_base64, des_cbc_decrypt_base64  
import base64

def client_program():
    host = socket.gethostname()  
    port = 5000  

    client_socket = socket.socket()  
    client_socket.connect((host, port))  

    key = "mysecret"  
    iv = "initvect"   

    message = input(" -> ")  

    while message.lower().strip() != 'bye':
        
        encrypted_message = des_cbc_encrypt_base64(message, key, iv)
        print("Sending encrypted message:", encrypted_message)
        client_socket.send(encrypted_message.encode())  

        
        data = client_socket.recv(1024).decode()
        print('Received from server (encrypted): ' + data)  

        
        decrypted_message = des_cbc_decrypt_base64(data, key, iv)
        print("Decrypted message from server:", decrypted_message)  

        message = input(" -> ")  

    client_socket.close()  


if __name__ == '__main__':
    client_program()
