from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
import os , socket
from pyftpdlib.servers import FTPServer

FTP_PORT = 8031
FTP_USER = 'user'
FTP_PASS = 'pass'
FTP_DIRECTORY = os.getcwd()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = s.getsockname()[0]

print(f'     ')
print(f'                 Welcome of Hacker      ')
print(f'                            ')
print(f'                      ╱▔▔▔▔▔▔▔▔╲              ')
print(f'                      ▏        ▕   ')
print(f'                     ▕ ╭━╮┈┈╭━╮▕             ')
print(f'                      ╲╰━╯╱╲╰━╯╱')
print(f'            _   2022   ▏╮┈▔▔┈╭▕   By: MRX~HACKS ')
print(f'           | \__________┣╋╋╋╋┫___________________')
print(f'        @8@8< ___________________________________\ ')
print(f'           |_/      ;;; ┣╋╋╋╋┫ ;;;')
print(f'      ▪             ;; ╲▂▂▂▂▂▂╱ ')
print(f'      ')
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
