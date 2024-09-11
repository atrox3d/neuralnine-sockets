import socket

import servercfg

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(servercfg.ADDRESS)

message = 'hello'
print(f'sending {message!r}...')
sent = client.send(message.encode())
print(f'{sent = }')

print('receving answer...')
answer = servercfg.receive_message(client)
print(f'{answer = }')

print('closing client')
client.close()
