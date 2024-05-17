#################################################################
# Console - Proy2 Expoandes: IntroISIS 2024-10
#################################################################

import config as cf
import sys

#################################################################
# imports

from src.objects.answerLog import AnswerLog
from src.objects.user import User

import pandas as pd
from pandas import DataFrame as df

import json
import hashlib
import os

assert cf

#################################################################

#Funciones de consola


def print_main_menu():
    
    print("\n")    
    print("Ingrese el tipo de usuario:")
    print("1 - Profesor")
    print("2 - Estudiante")
    print("3 - Registrarse")
    print("4 - Salir")
    
def register_user(user_type, username, password):
    if user_exists(user_type, username):
        print("Username already exists.")
        return False

    hashed_password = hash_password(password)
    save_user_details(user_type, username, hashed_password)
    print(f"{user_type.capitalize()} registered successfully.")
    return True

# Function to check if a user already exists
def user_exists(user_type, username):
    if not os.path.exists(USER_DATA_FILE):
        return False

    with open(USER_DATA_FILE, 'r') as file:
        data = json.load(file)
    
    if user_type in data and username in data[user_type]:
        return True
    return False

# Function to hash the password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to save user details to the JSON file
def save_user_details(user_type, username, hashed_password):
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as file:
            data = json.load(file)
    else:
        data = {"students": {}, "profesors": {}, "log": {}}

    if user_type not in data:
        data[user_type] = {}
        
    data[user_type][username] = {}
    data[user_type][username]["password"] = hashed_password

    with open(USER_DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Function to authenticate a user
def authenticate_user(user_type, username, password):
    if not user_exists(user_type, username):
        print("Username does not exist.")
        return False

    with open(USER_DATA_FILE, 'r') as file:
        data = json.load(file)

    hashed_password = hash_password(password)
    if data[user_type][username]["password"] == hashed_password:
        print("Login successful.")
        return True
    else:
        print("Invalid password.")
        return False
    
#################################################################

USER_DATA_FILE = 'database.json'

if __name__ == "__main__":
    """
    Menu principal
    """
    def menu_cycle():
        
        working = True
        #ciclo del menu
        while working:
            
            print_main_menu()            
            
            inputs = input('\n Seleccione una opción para continuar: ')
            
            if int(inputs) == 1:
                
                print("\nLog In Profesores \n")
                username = input("ingrese el nombre de usuario: ")
                password = input("ingrese la contraseña: ")
                success = authenticate_user("profesors", username, password)
                
                
            elif int(inputs) == 2:
                
                print("\n Log In Estudiantes \n")
                username = input("ingrese el nombre de usuario: ")
                password = input("ingrese la contraseña: ")
                authenticate_user("estudents",username, password)
                    
            
            elif int(inputs) == 3:
                print("\nRegistro\n")
                print("1 - registrar profesor")
                print("2 - registrar estudiante")
                
                option = input("Ingrese el tipo de registro: ")

                if int(option) == 1:
                
                    user_type = "profesors"
                    username = input("ingrese el nombre de usuario: ")
                    password = input("ingrese la contraseña: ")
                    register_user(user_type, username, password)
                    
                elif int(option) == 2:
                    
                    user_type = "estudents"
                    username = input("ingrese el nombre de usuario: ")
                    password = input("ingrese la contraseña: ")
                    register_user(user_type, username, password)
                    
                else:
                    
                    print("Opcion invalida")
                
            elif int(inputs) == 4:
                
                print("\nGracias por utilizar el programa") 
                
                working = False
            
            else:
                
                print("\nOpción errónea, vuelva a intentarlo.\n")
                
        sys.exit(0)
        
    menu_cycle()
