import socket
import logging


def setup_logger(name:str) -> logging.Logger:
    logging.basicConfig(
        level=logging.INFO,
        format=(
            '%(levelname)-8s | '
            '%(filename)-10s | '
            '%(message)s'
        )
    )
    return logging.getLogger(name)

def get_ipaddress() -> str:
    ''' does not work with virtualbox network adapter '''
    hostname = socket.gethostname()
    address = socket.gethostbyname(hostname)
    return address

def receive_message(endpoint:socket.socket, buffer=1024):
    logger.info('receiving...')
    return endpoint.recv(buffer).decode()

logger = setup_logger(__name__)







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
