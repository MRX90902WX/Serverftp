from os import system
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
import os , socket
from pyftpdlib.servers import FTPServer

system("clear")
print(f'\u001b[32;1m __  __ ____  __  __')
print(f'\u001b[32;1m|  \/  |  _ \ \ \/ /')
print(f'\u001b[32;1m| |\/| | |_) | \  /')
print(f'\u001b[32;1m| |  | |  _ <  /  \ ')
print(f'\u001b[32;1m|_|  |_|_| \_\/_/\_\ ')
print(f' ')

FTP_DIRECTORY = input("\u001b[32;1m[+]Ingrese el directorio que desea exponer : ")

FTP_PORT = input("\u001b[32;1m[+]Ingrese un puerto def.[4444] : ")
FTP_USER = input("\u001b[32;1m[+]Ingrese un usuario a guardar : ")
FTP_PASS = input("\u001b[32;1m[+]Ingrese un passwd a guardar  : ")
FTP_SERVER = input("\u001b[32;1m[+]Nombre del servidor FTP : ")

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
print(f'            _   2023   ▏╮┈▔▔┈╭▕   By: MRX~HACKS ')
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
handler.banner = (FTP_SERVER)
handler.passive_ports = range(60000, 65535)

address = ('', FTP_PORT)
server = FTPServer(address, handler)

server.max_cons = 4000000
server.max_cons_per_ip = 15

server.serve_forever()
