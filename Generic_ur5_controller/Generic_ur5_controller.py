import time
import serial
from math import pi
import numpy
import socket

import waypoints as wp
import kg_robot as kgr


def main():
    print("------------Configuring Burt-------------\r\n")
    burt = kgr.kg_robot(port=30010,db_host="192.168.1.10")
    #burt = kgr.kg_robot(port=30010,ee_port="COM32",db_host="192.168.1.51")
    print("----------------Hi Burt!-----------------\r\n\r\n")

    try:
        while 1:
            ipt = input("cmd: ")
            if ipt == 'close':
                break
            elif ipt == 'home':
                burt.home()
            elif ipt == 'rec':
                burt.teach_mode.record()
            elif ipt == 'play':
                burt.teach_mode.play()

            else:
                var = int(input("var: "))
                burt.serial_send(ipt,var,True)

        
    finally:
        print("Goodbye")
        burt.close()
if __name__ == '__main__': main()
