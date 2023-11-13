import argparse
import subprocess
import sys
from os.path import join

def script1():
    subprocess.run(["python", "script1.py"])

def script2():
    subprocess.run(["python", "script2.py"])

def script3():
    subprocess.run(["python", "script3.py"])

def script4():
    subprocess.run(["python", "script4.py"])

def script5():
    subprocess.run(["python", "script5.py"])

def script6():
    subprocess.run(["python", "script6.py"])

def script7():
    subprocess.run(["python", "script7.py"])

def main():
    parser = argparse.ArgumentParser(description="Menú de Scripts")

    subparsers = parser.add_subparsers(title="Scripts", dest="script")
    subparsers.required = True

    # Script 1
    parser_script1 = subparsers.add_parser("script1", help="Analisis URL")

    # Script 2
    parser_script2 = subparsers.add_parser("script2", help="Cifrado de archivos")

    # Script 3
    parser_script3 = subparsers.add_parser("script3", help="Envio de correo")

    # Script 4
    parser_script4 = subparsers.add_parser("script4", help="Web scraping")

    # Script 5
    parser_script5 = subparsers.add_parser("script5", help="Escaneo de Red")

    # Script 6
    parser_script6 = subparsers.add_parser("script6", help="Prueba pow pyt")

    # Script 7
    parser_script7 = subparsers.add_parser("script7", help="Escan Puert Arg")

    args = parser.parse_args()

    # Ejecuta el script correspondiente
    if args.script == "script1":
        script1()
    elif args.script == "script2":
        script2()
    elif args.script == "script3":
        script3()
    elif args.script == "script4":
        script4()
    elif args.script == "script5":
        script5()
    elif args.script == "script6":
        script6()
    elif args.script == "script7":
        script7()

if __name__ == "__main__":
    main()
