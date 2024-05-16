#################################################################
# Console - Proy2 Expoandes: IntroISIS 2024-10
#################################################################

import sys
import config as cf

#################################################################
# imports

from src.objects.answerLog import AnswerLog
from src.objects.user import User

import pandas as pd
from pandas import DataFrame as df

assert cf

#################################################################

#Funciones de consola


def printMenuUsers():
    
    print("\n")    
    print("Ingrese el tipo de usuario:")
    print("1 - Profesor")
    print("2 - Estudiante")
    print("3 - Salir")
    print("\n")


def registro():
    
    tipo = input("Ingrese el tipo de usuario")
    username = input("ingrese el nombre de usuario")
    password = input("ingrese la contraseña")
    
#################################################################

if __name__ == "__main__":
    """
    Menu principal
    """
    def menuCycle():
        working = True
        #ciclo del menu
        while working:
            printMenuUsers()
            
            
            inputs = input('Seleccione una opción para continuar\n')
            
            if int(inputs) == 1:
                
                print("Log In Profesores \n")
                
            elif int(inputs) == 2:
                
                print("Log In Estudiantes \n")     
            
            elif int(inputs) == 4:
                
                registro()
                
            elif int(inputs) == 3:
                
                print("\nGracias por utilizar el programa") 
                
                working = False
            
            else:
                print("Opción errónea, vuelva a intentarlo.\n")
        sys.exit(0)
        
    menuCycle()
