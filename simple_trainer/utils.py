import os

def str_input(text):
    res = input(text)
    while len(res.strip()) == 0:
        res = input(text)
    return res

def int_input(text):
    while True:
        try:
            res = int(input(text))
            return res
        except:
            pass

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
