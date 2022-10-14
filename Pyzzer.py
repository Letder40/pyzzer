#!/bin/env python3
import os
import sys
import re
import platform
from colorama import init, Fore, Back, Style

init(autoreset=True)

sistema = platform.system()

text_error = Fore.RED + '[!] error:' + Style.RESET_ALL 
prompt = Fore.GREEN + "-> " + Style.RESET_ALL 
def clear():
    if sistema == "Linux":
        os.system("clear")
    if sistema == "Windows":
        os.system("cls")

def help():
    for i in sys.argv:
        print(" -> test")
        print(" -> create")
        print(" -> use")
        print(" -> interactive")

#ls function 
def ls():
    if sistema == "Linux":
        os.system("ls ./quizes/")
    elif sistema == "Windows":
        os.system("dir ./quizes/")

    input(Fore.YELLOW + "\npulsa enter para continuar [ <--| ]")
    clear()
    console()

#create function 
def create():
     
    error = True
    while(error):
        file_name = input(Fore.CYAN + "Nombre del quizz?" + Style.RESET_ALL + "\n" + prompt)
        if os.path.exists("./quizzes/" + file_name):
            error = True
            print(text_error + " Ya hay un archivo con ese nombre")
        else:
            error = False
         

    error = True
    while(error):
        try:
            numero_preguntas = int(input(Fore.CYAN + "¿Cuantas preguntas va a tener el quizz?" + Style.RESET_ALL + "\n" + prompt))
            error = False
        except:
            error = True
            print(text_error + " Ingresa un numero")

    preguntas = []
    respuestas = []

    for i in range(numero_preguntas):
        preguntas.append(input(Fore.YELLOW + "pregunta "+ str(i+1) + Style.RESET_ALL + "\n" + prompt))
        respuestas.append(input(Fore.YELLOW + "respuesta " + Style.RESET_ALL + "\n" + prompt))  
        if i+1 == numero_preguntas:
            clear()
            print(Fore.CYAN + "[#] Quizz generado \n")
            number = 1
            for pregunta in preguntas:
                print(str(number) + ". " + pregunta)
                print("   " + respuestas[number-1])
                number = number + 1

            save = input(Fore.YELLOW + "[!]" + Style.RESET_ALL + " quieres guardar este test? [yes] [no] " + "\n" +  prompt)
            if save == "yes" or save == "y" or save == "YES":
                number = 1
                f = open("./quizes/" + file_name , "a")
                for pregunta in preguntas:
                    f.write(str(number) + ". " + pregunta + "\n")
                    f.write("   " + respuestas[number-1] + "\n")
                    number = number + 1
                print(Fore.GREEN + "\n guardado \n")
                input(Fore.YELLOW + "pulsa enter para continuar [ <--| ]")
    clear() 
    console()

#use function
def use():
    error = True
    while(error):
        file_name = input(Fore.CYAN + "Nombre del quizz a usar?" + Style.RESET_ALL + "\n" + prompt)
        if os.path.exists("./quizes/" + file_name):
            error = False
        else:
            error = True
            print(text_error + " No hay un archivo con ese nombre")
    file = open("./quizes/" + file_name, "r")
    
    content = []
    number_lines = 0
    cleaner = re.compile("\s\s\s|\n")
    for i in file:
        i = cleaner.sub("",i)
        content.append(i)
        number_lines = number_lines + 1

    clear()

    aciertos = []
    questions = []
    questions_pointer = 1
    for i in range(number_lines):
        if i % 2 == 0:
            questions.append(content[i])
            print(Fore.YELLOW + content[i])
            respuesta = input(prompt)
            if respuesta.lower() == content[i+1].lower():
                aciertos.append(questions_pointer)
            else:
                aciertos.append("")
            questions_pointer = questions_pointer + 1
    
    clear()

    nota = 0
    si = 0
    number_questions = questions_pointer - 1
    print(Fore.CYAN + "RESULTADOS: \n")
    for i in questions:
        if aciertos[si] == si + 1:
            print(questions[si] + Fore.GREEN + " correcto")
            nota = nota + 1
        else:
            print(questions[si] + Fore.RED + " incorrecto")
        si = si + 1
    nota_final = nota / number_questions * 10
    if(nota_final >= 5):
        print("\n" + Fore.YELLOW + "[#] Tu nota es = " + Fore.GREEN + str(nota) + Style.RESET_ALL + "/"+str(number_questions) + " -> " + Fore.GREEN + str(nota_final))
    else:
        print("\n" + Fore.YELLOW + "[#] Tu nota es = " + Fore.RED + str(nota) + Style.RESET_ALL + "/"+str(number_questions) + " -> " + Fore.RED + str(nota_final))
    input(Fore.YELLOW + "\npulsa enter para continuar [ <--| ]")
    clear()
    console()

#console function
def console():
    print(Fore.YELLOW + "[!] Selector de modos\n")
    print(Fore.CYAN + "[#] modos: ")
    print("1 ->" + Fore.GREEN + " usar:" + Style.RESET_ALL + " empieza un nuevo intento a uno de tus quizzes")
    print("2 ->" + Fore.GREEN + " crear:" + Style.RESET_ALL + " crea un nuevo quizz")
    print("3 ->" + Fore.GREEN + " list:" + Style.RESET_ALL + " muestra todos tus quizzes")
    print("4 ->" + Fore.GREEN + " exit:" + Style.RESET_ALL + " cerrar Pyzzer")
    error = True
    while(error):
        mode = input("\nSelecciona un modo" + "\n" + prompt)
        if mode == "1" or mode == "usar":
            error = False
            clear()
            use()
        elif mode == "2" or mode == "crear":
            error = False
            clear()
            create()
        elif mode == "3" or mode == "list" or mode == "ls":
            error = False
            clear()
            ls()
        elif mode == "4" or mode == "exit":
            exit()
        else:
            error = True
            print(text_error + " no has elegido una opción válida")
#CAPTCHING ARGUMENTS
try:
    arg1 = sys.argv[1]
except:
    arg1 = "no_arg1"

if arg1 == "test":
    print("funciono")

elif arg1 == "use":
    clear()
    use()
    
elif arg1 == "create":
    clear()
    create() 
        
elif arg1 == "interactive":
    clear()
    console()
#default
elif arg1 == "no_arg1":
    clear()
    console()
else:
    print(" [#] No se ha dado ninguna oppción aquí tienes una lista de opciones validas")
    help()
