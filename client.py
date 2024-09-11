import socket
import time

import config
import helpers

logger = helpers.setup_logger(__name__)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# SERVER = socket.gethostbyname(socket.gethostname())
SERVER = 'server'
ADDRESS = (SERVER, config.PORT) 
retry = True
while retry:
    try:
        logger.info(f'connecting to {ADDRESS}...')
        server.connect(ADDRESS)
        retry = False
    except ConnectionRefusedError as cre:
        print(cre,)
        time.sleep(3)
        print('retrying')

message = 'hello'
logger.info(f'sending {message!r}...')
sent = server.send(message.encode())
logger.info(f'{sent = }')

logger.info('receving answer...')
# logger.info(server.recv(1024))
answer = helpers.receive_message(server)
logger.info(f'{answer = }')
logger.info('closing client')
server.close()
