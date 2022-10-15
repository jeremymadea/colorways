from zipfile import ZipFile
import os

def make():
    z = os.path.join(os.path.dirname(os.path.realpath(__file__)),"demos.zip")
    ZipFile(z).extractall()

if __name__ == '__main__':
    make()
