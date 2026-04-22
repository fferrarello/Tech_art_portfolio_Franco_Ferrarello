import sys
import os

def install(path):
    if path not in sys.path:
        sys.path.append(path)
        print("TAProSuite instalado correctamente")