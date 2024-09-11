import socket
import servercfg


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(servercfg.ADDRESS)
server.listen(5)
try:
    while True:
        print('waiting for connections...')
        client, address = server.accept()
        print(f'connected to {address}')

        print(f'receiving message from {address}...')
        message = servercfg.receive_message(client)
        print(f'{message = }')

        print(f'answering to {address}')
        client.send(f'message received.'.encode())
        
        client.close()
        print(f'connection with {address} closed.')
except KeyboardInterrupt:
    print('\nshutting down server')
    server.close()
