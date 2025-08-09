import socket as _socket, struct, dill
from typing import Generator

def socket(timeout:int=10):
    s = _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)
    s.settimeout(timeout)
    return s

class conn:

    def __init__(self, conn:_socket.socket):
        self.conn = conn

    def send(self, data):

        data = dill.loads(data)

        # Pack the length into a 4-byte header (e.g., using '!' for network byte order, 'I' for unsigned int)
        header = struct.pack('!I', len(data))

        # Send the header
        self.conn.sendall(header)

        # Send the actual data
        self.conn.sendall(data)

    def recv(self):

        # Unpack the length from the header
        length = struct.unpack('!I', 
            self.conn.recv(4)
        )[0]

        # Receive the actual data based on the unpacked length
        data = self.conn.recv(length).decode('utf-8')

        return dill.loads(data)

class host:

    def __init__(self, port:int):
        self.bindings = ('127.0.0.1', port)
        self.s = _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)
        self.start()
    
    def close(self):
        self.s.close()
        self.started = False

    def start(self):
        try:
            self.s.bind(self.bindings)
            self.s.listen()

            self.started = True
        except:
            self.started = False
            return

    def listen(self) -> Generator[conn]:
        while True:
            yield conn(self.s.accept()[0])

def client(ip:str, port:int):
    try:
        conn_ = socket()
        conn_.connect((ip, port))
        return conn(conn_)
    except:
        return None
