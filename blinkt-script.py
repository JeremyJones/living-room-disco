from blinkt import *
from datetime import datetime as dt
from time import sleep


def cycle_full(iterations=12, delay=0.25, brightness=1):
    curiter = 0

    while curiter < iterations:
        set_all(255,0,0,brightness)
        show()
        sleep(delay)
        set_all(0,0,255,brightness)
        show()
        sleep(delay)
        set_all(0,255,0,brightness)
        show()
        sleep(delay)
        curiter += 1

    clear()
    show()


    
    
def main():
    while True:
        cycle_full()
    
    

if __name__ == "__main__":
    main()
