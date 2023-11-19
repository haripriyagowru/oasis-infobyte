import socket
import threading

# Client configuration
HOST = '127.0.0.1'
PORT = 12345

# Create a socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(message)
        except:
            print('An error occurred!')
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('utf-8'))

# Set a nickname for the client
nickname = input('Enter your nickname: ')

# Create separate threads for receiving and sending messages
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
