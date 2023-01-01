#! /usr/bin/python3
# -*- coding: utf-8 -*-

__description__ = 'este modulo se usa para imprimir colores'
__license__ = 'Apache 2.0'
__title__ = 'Color'
cryptography_version = '2.0.0'
__copyright__ = 'Desmon'

class COLOR:
          
    def __init__(self):
       
        self.BLACK           =  "\033[30m"
        self.RED             =  "\033[31m"
        self.GREEN           =  "\033[32m"
        self.YELLOW          =  "\033[33m"
        self.BLUE            =  "\033[34m"
        self.MAGENTA         =  "\033[35m"
        self.CYAN            =  "\033[36m"
        self.WHITE           =  "\033[37m"
        self.RESET           =  "\033[39m"

        self.LIGHTBLACK_EX   =  "\033[90m"
        self.LIGHTRED_EX     =  "\033[91m"
        self.LIGHTGREEN_EX   =  "\033[92m"
        self.LIGHTYELLOW_EX  =  "\033[93m"
        self.LIGHTBLUE_EX    =  "\033[94m"
        self.LIGHTMAGENTA_EX =  "\033[95m"
        self.LIGHTCYAN_EX    =  "\033[96m"
        self.LIGHTWHITE_EX   =  "\033[97m"

    def UP(self, n=1):
        return '\033[' + str(n) + 'A'
    def DOWN(self, n=1):
        return '\033[' + str(n) + 'B'
    def FORWARD(self, n=1):
        return '\033[' + str(n) + 'C'
    def BACK(self, n=1):
        return '\033[' + str(n) + 'D'
    def POS(self, x=1, y=1):
        return '\033[' + str(y) + ';' + str(x) + 'H'
    def SET_TITLE(self, text):
        return "\033]2;{}\007".format(text)
    def CLEAR(self):
        return "\033[3J\033[H\033[2J"
    def POINTGREEN(self, text1="", text2=""):
        return self.LIGHTGREEN_EX+"["+self.BLUE+"*"+self.LIGHTGREEN_EX+"] "+self.LIGHTWHITE_EX+text1+text2+self.LIGHTWHITE_EX
    def POINTRED(self, text=""):
        return self.LIGHTYELLOW_EX+"["+self.RED+"*"+self.LIGHTYELLOW_EX+"] "+self.LIGHTMAGENTA_EX+text+"\n"+self.LIGHTWHITE_EX

if __name__ == "__main__":
    colors = COLOR()

    print(colors.CLEAR())

    print("{} colors.BLACK".format(colors.BLACK))
    print("{} colors.RED".format(colors.RED))
    print("{} colors.GREEN".format(colors.GREEN))
    print("{} colors.YELLOW".format(colors.YELLOW))
    print("{} colors.MAGENTA".format(colors.MAGENTA))
    print("{} colors.CYAN".format(colors.CYAN))
    print("{} colors.WHITE".format(colors.WHITE))
    print("{} colors.RESET".format(colors.RESET))

    print("{} colors.LIGHTBLACK_EX".format(colors.LIGHTBLACK_EX))
    print("{} colors.LIGHTRED_EX".format(colors.LIGHTRED_EX))
    print("{} colors.LIGHTGREEN_EX".format(colors.LIGHTGREEN_EX))
    print("{} colors.LIGHTYELLOW_EX".format(colors.LIGHTYELLOW_EX))
    print("{} colors.LIGHTBLUE_EX".format(colors.LIGHTBLUE_EX))
    print("{} colors.LIGHTMAGENTA_EX".format(colors.LIGHTMAGENTA_EX))
    print("{} colors.LIGHTCYAN_EX".format(colors.LIGHTCYAN_EX))
    print("{} colors.LIGHTWHITE_EX".format(colors.LIGHTWHITE_EX))
    print("{} colors.RESET".format(colors.RESET))

    print(colors.SET_TITLE("modulo colors"))
    print(colors.POINTGREEN("Texto 1"))
    print(colors.POINTRED("Texto 2"))
