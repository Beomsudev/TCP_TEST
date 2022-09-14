import socket
import time


class KeyenceTtl():
    def __init__(self):
        self.host = '169.254.0.2'
        self.port = 9004
        self.skt = socket.socket()

    def hook(self):
        start_time = time.time()

        code = self.get_code()

        arrange_code = self.arrange_code(code)

        end_time = time.time()
        tact_time = end_time - start_time
        print(f"\n\ntact time {tact_time} : sec")

    def get_code(self):
        host = self.host
        port = self.port
        self.skt.connect((host, port))
        self.skt.settimeout(1000)

        print('*****READ START*****')
        self.skt.send(b"LON\r")
        time.sleep(0.5)
        self.skt.send(b"LOFF\r")
        print('*****READ E N D*****')

        code = self.skt.recv(9004).decode('utf-8')
        # print(code)

        self.skt.close()

        return code

    @staticmethod
    def arrange_code(code):
        sepa = code.strip().split(',')
        '''
        CODE ORIGINAL SAMPLE
        
        CRA370820!66 / 999, P1735623 - 01 - A: SBYA2216500050X!330 / 959, P1735623 - 01 - A: SBYA2
        216500050
        W!331 / 309, P1735623 - 01 - A: SBYA2216500050Y!777 / 956, P1735623 - 01 - A: SBY
        A2216500051W!780 / 300, P1735623 - 01 - A: SBYA22165000516!1241 / 294, P1735623 - 01 - A:
        SBYA2216500051S!1241 / 959, P1735623 - 01 - A: SBYA2216500050Z!1715 / 292, P1735623 - 0
        1 - A: SBYA2216500051T!1715 / 962, P1735623 - 01 - A: SBYA22165000514!2191 / 289, P17356
        23 - 01 - A: SBYA22165000512!2191 / 964
        '''
        code_list = []
        for i in sepa:
            code_sepa = i.split('!')
            code_list.append(code_sepa)

        print(code_list)

        '''
        CODE LIST SAMPLE
        [
        ['CRA370820', '66/999'],
        ['P1735623-01-A:SBYA2216500050X', '330/959'],
        ['P1735623-01-A:SBYA2216500050W', '331/309'],
        ['P1735623-01-A:SBYA2216500050Y', '777/956'],
        ['P1735623-01-A:SBYA2216500051W', '780/300'],
        ['P1735623-01-A:SBYA22165000516', '1241/294'],
        ['P1735623-01-A:SBYA2216500051S', '1241/959'],
        ['P1735623-01-A:SBYA2216500050Z', '1715/292'],
        ['P1735623-01-A:SBYA2216500051T', '1715/962'],
        ['P1735623-01-A:SBYA22165000514', '2191/289'],
        ['P1735623-01-A:SBYA22165000512', '2191/964'],
        ]      
        '''


if __name__ == "__main__":
    KeyenceTtl().hook()