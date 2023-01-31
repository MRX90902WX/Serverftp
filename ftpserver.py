from os import system
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
import os , socket
from pyftpdlib.servers import FTPServer

system("clear")
print(f'__  __ ____  __  __')
print(f'|  \/  |  _ \ \ \/ /')
print(f'| |\/| | |_) | \  /')
print(f'| |  | |  _ <  /  \ ')
print(f'|_|  |_|_| \_\/_/\_\ ')
print(f' ')

FTP_DIRECTORY = input("\u001b[32;1m[+]Ingrese el directorio que desea exponer > ")
FTP_PORT = 4444
FTP_USER = 'admin'
FTP_PASS = 'admin'

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
print(f'           |_/          ┣╋╋╋╋┫  ')
print(f'                       ╲▂▂▂▂▂▂╱ ')
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
