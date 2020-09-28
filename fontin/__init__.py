import sys, os, ctypes

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False