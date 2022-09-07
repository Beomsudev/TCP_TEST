import socket
import time


class KeyenceTtl():
    def __init__(self):
        self.host = '169.254.0.2'
        self.port = 9004
        self.skt = socket.socket()

    def get_code(self):
        self.skt.connect(('169.254.0.2', 9004))
        self.skt.settimeout(1000)

        print('*****START*****')
        self.skt.send(b"LON\r")
        time.sleep(0.5)
        self.skt.send(b"LOFF\r")
        print('*****E N D*****')


        print(self.skt.recv(1024).decode('utf-8'))
        self.skt.close()


if __name__ == "__main__":
    KeyenceTtl().get_code()

