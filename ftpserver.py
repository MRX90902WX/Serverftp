from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
import os , socket
from pyftpdlib.servers import FTPServer

FTP_PORT = 8021
FTP_USER = 'user'
FTP_PASS = 'pass'
FTP_DIRECTORY = os.getcwd()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = s.getsockname()[0]
s.close()


print(f'DIRECCION: ftp://{IP}:{FTP_PORT}')
print(f'DIRECTORIO RAIZ: {FTP_DIRECTORY}')


authorizer = DummyAuthorizer()
authorizer.add_user(FTP_USER, FTP_PASS, FTP_DIRECTORY, perm='elradfmw')

handler = FTPHandler
handler.authorizer = authorizer
handler.banner = 'Termux FTP Server :D'
handler.passive_ports = range(50000, 55535)

address = ('', FTP_PORT)
server = FTPServer(address, handler)

server.max_cons = 256
server.max_cons_per_ip = 5

server.serve_forever()
