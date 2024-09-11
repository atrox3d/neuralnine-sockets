import socket

import config
import helpers

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.connect(config.ADDRESS)

message = 'hello'
print(f'sending {message!r}...')
sent = server.send(message.encode())
print(f'{sent = }')

print('receving answer...')
# print(server.recv(1024))
answer = helpers.receive_message(server)
print(f'{answer = }')
print('closing client')
server.close()
