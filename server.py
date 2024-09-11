import socket

import config
import helpers

logger = helpers.setup_logger(__name__)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(config.ADDRESS)
server.listen(5)
try:
    while True:
        logger.info('waiting for connections...')
        client, address = server.accept()
        logger.info(f'connected to {address}')

        logger.info(f'receiving message from {address}...')
        message = helpers.receive_message(client)
        logger.info(f'{message = }')

        logger.info(f'answering to {address}')
        client.send(f'message received.'.encode())
        
        client.close()
        logger.info(f'connection with {address} closed.')
except KeyboardInterrupt:
    logger.info('\nshutting down server')
finally:
    logger.info('closing connection')
    server.close()

