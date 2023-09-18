try:
    import termios
    import tty
    import sys

    def getkey():
        termios.get()

except ImportError as e:
    import msvcrt
    
    def getkey():
        msvcrt.getch()

finally:
    getkey()
