from estrutura.interface import *
from sys import platform


interface = InterfaceMEPB_Windows() if platform == 'win32' else InterfaceMEPB_Linux()