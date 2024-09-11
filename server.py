import socket

def get_ipaddress() -> str:
    ''' does not work with virtualbox network adapter '''
    hostname = socket.gethostname()
    address = socket.gethostbyname(hostname)
    return address

def receive_message(client:socket.socket, buffer=1024):
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

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)
try:
    while True:
        client, address = server.accept()
        print(f'connected to {address}')

        message = receive_message(client)
        print(f'{message = }')

        client.send(f'message received.'.encode())
        
        client.close()
        print(f'connection with {address} closed.')
except KeyboardInterrupt:
    print('\nshutting down server')
    server.close()
