import socket

def get_ipaddress() -> str:
    ''' does not work with virtualbox network adapter '''
    hostname = socket.gethostname()
    address = socket.gethostbyname(hostname)
    return address

def receive_message(client:socket.socket, buffer=1024):
    return client.recv(buffer).decode()
    message = ''
    while True:
        chunk = client.recv(buffer).decode()
        if len(chunk) < 1:
            break
        message += chunk
    return message

# HOST = get_ipaddress()
HOST = 'localhost'
PORT = 9090
ADDRESS = (HOST, PORT)
