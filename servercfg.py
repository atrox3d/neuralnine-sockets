import socket

def get_ipaddress() -> str:
    ''' does not work with virtualbox network adapter '''
    hostname = socket.gethostname()
    address = socket.gethostbyname(hostname)
    return address

def _receive_message(endpoint:socket.socket, buffer=1024):
    endpoint.settimeout(None)
    message = ''
    while True:
        try:
            print('waiting for recv...')
            data = endpoint.recv(buffer).decode()
            print(f'received {len(data)} bytes: {data}')
            if not data:
                print('no data received')
                break
        except socket.timeout:
            print('reached timeout while waiting for data')
            break
        # if len(data) < 1:
            # break
        message += data
    return message

def receive_message(endpoint:socket.socket, buffer=1024):
    return endpoint.recv(buffer).decode()

# HOST = get_ipaddress()
HOST = 'localhost'
PORT = 9090
ADDRESS = (HOST, PORT)
