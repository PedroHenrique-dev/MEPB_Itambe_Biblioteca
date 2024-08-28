from src.interface import *
from sys import platform

if __name__ == '__main__':
    interface = InterfaceMEPB_Windows() if platform == 'win32' else InterfaceMEPB_Linux()
