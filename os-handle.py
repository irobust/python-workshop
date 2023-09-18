try:
    import termios
    import tty
    import sys
except ImportError as e:
    import msvcrt
    print(e)
