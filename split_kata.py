DAKUTEN = "ガギグゲゴザジズゼゾダヂヅデドバビブベボ"
HANDAKUTEN = "パピプペポ"

def split_kata(input):
    """splits dakuten and handakuten from katakana"""
    return_str = ""
    for x in input:
        if x in DAKUTEN:
            return_str += chr(ord(x)-1) + "゛"
        elif x in HANDAKUTEN:
            return_str += chr(ord(x)-2) + "゜"
        else:
            return_str += x
    return return_str