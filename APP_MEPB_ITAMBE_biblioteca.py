from sys import platform

from src.interface import InterfaceMEPB_Windows, InterfaceMEPB_Linux

if __name__ == '__main__':
    interface = InterfaceMEPB_Windows() if platform == 'win32' else InterfaceMEPB_Linux()
