import os
import platform

sistema = platform.system()

if sistema == "Darwin":
    os.system("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py")
    os.system("python3 get-pip.py")
    os.system("rm get-pip.py")
    os.system("python3 -m pip install colorama")
    input("All went without any problem, thank you so much for install pyzzer, enjoy :D")
    exit(0)
    
try:
    os.system("pip install colorama")
    input("All went without any problem, thank you so much for install pyzzer, enjoy :D")
except:
    print("something went wrong")
    input("Instalación manual -> Abre tu terminal y ejecuta esta comando: pip install colorama")