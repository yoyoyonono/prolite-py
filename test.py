from typing import List
import serial
from sign import Sign
import PIL.Image
import os
import time

from split_kata import split_kata

com_port = 'COM6'
sign_id = '01'
baud_rate = 9600

def load_char(char_id: str):    
    char = PIL.Image.open(f'font/{char_id}.bmp')
    char_data = [['B'] * 6 for _ in range(7)]
    for x in range(0, char.size[0]):
        for y in range(0, char.size[1]):
            print(char.getpixel((x, y)), end='')
            if char.getpixel((x, y)) != 0:
                char_data[y][x] = 'G'
        print()
    return char_data

def char_to_string(char: List[List[str]]):
    return (''.join([''.join(line) for line in char]))

def assemble_chars(char1: List[List[str]], char2: List[List[str]], char3: List[List[str]]):
    """Adds rows of lists of char1, char2, char3 together into one larger list of lists"""
    return [line1 + line2 + line3 for line1, line2, line3 in zip(char1, char2, char3)]

CHARS = {}

for x in os.listdir('./font/'):
    CHARS[x[:-4]] = load_char(x[:-4])

def display_jp(sign: Sign, text: str):
    """Displays a string of Japanese characters"""
    text = split_kata(text)
    text = text.rjust(len(text) + (3 - len(text)%3), '　')
    for x in range(0, len(text), 3):
        char1 = CHARS[text[x]]
        char2 = CHARS[text[x + 1]]
        char3 = CHARS[text[x + 2]]
        print(chr(65 + x//3))
        sign.create_graphic(chr(65 + x//3), char_to_string(assemble_chars(char1, char2, char3)))
    time.sleep(0.2)
    sign.send_text('A', '<FX>' + ''.join(f'<B{chr(65 + x)}>' for x in range(len(text)//3)) + ' ' * 10)

port = serial.Serial(com_port, baud_rate, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
sign = Sign(port, '01', 9600)
display_jp(sign, ('アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲンァィゥェォッャュョ゛゜。・、「」千万円馬尺'))
#display_jp(sign, 'アキハバラ馬尺')
#while x := input():
#    sign.wake_up()
#    sign.send_text('A', x)
####
#sign.create_graphic('A', char_to_string(assemble_chars(CHARS['ア'], CHARS['イ'], CHARS['イ'])))
#sign.send_text('A', '<BA>')
####
#sign.send_text('A', ' '.join(f'<B{chr(x)}>' for x in range(65, 91)))
port.close()