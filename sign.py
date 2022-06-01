import serial
import time

class Sign:
    def __init__(self, serial_port: serial.Serial, sign_id: str, baud_rate: int):
        self.serial_port = serial_port
        self.sign_id = sign_id
        self.baud_rate = baud_rate
    
    def __send_command(self, command):
        self.serial_port.write(f'{command}\r\n'.encode('utf-8'))
        time.sleep(0.1)

    def send_command(self, command):
        self.__send_command(f'<ID{self.sign_id}>{command}')

    def create_graphic(self, page:str, graphic:str):
        self.__send_command(f'<ID{self.sign_id}><G{page}>{graphic}')

    def clear_graphics(self):
        self.__send_command(f'<ID{self.sign_id}><DG*>')

    def clear_page(self, page:str):
        self.__send_command(f'<ID{self.sign_id}><DP{page}>')

    def send_text(self, page:str, text:str):
        self.__send_command(f'<ID{self.sign_id}><P{page}>{text}')
    
    def wake_up(self):
        self.__send_command(f'<ID{self.sign_id}>')
    