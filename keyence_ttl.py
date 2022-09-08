import socket
import time


class KeyenceTtl():
    def __init__(self):
        self.host = '169.254.0.2'
        self.port = 9004
        self.skt = socket.socket()

    def hook(self):
        code = self.get_code()

        arrange_code = self.arrange_code(code)



    def get_code(self):
        host = self.host
        port = self.port
        self.skt.connect((host, port))
        self.skt.settimeout(1000)

        print('*****START*****')
        self.skt.send(b"LON\r")
        time.sleep(0.5)
        self.skt.send(b"LOFF\r")
        print('*****E N D*****')

        code = self.skt.recv(7004).decode('utf-8')
        # print(code)

        self.skt.close()

        return code

    def arrange_code(self, code):
        print(code)
        print(type(code))

        print("**********")
        sepa = code.split(',')
        print(sepa)
        print(type(sepa))


if __name__ == "__main__":
    KeyenceTtl().hook()



