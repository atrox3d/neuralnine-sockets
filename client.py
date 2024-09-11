import socket

import servercfg

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.connect(servercfg.ADDRESS)

message = 'hello'
print(f'sending {message!r}...')
sent = server.send(message.encode())
print(f'{sent = }')

print('receving answer...')
# print(server.recv(1024))
answer = servercfg.receive_message(server)
print(f'{answer = }')
print('closing client')
server.close()
