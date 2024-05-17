#################################################################
# console (test_file) - Proy2 Expoandes: IntroISIS 2024-10
#################################################################

import config as cf

#################################################################
# imports

from src.objects.answerLog import AnswerLog
from src.objects.user import User

import pandas as pd
import datetime
import time
import csv
from pandas import DataFrame as df

assert cf

#################################################################
# persitencia

RECORDS_CSV_FILE = "study_records.csv"

def save_records_to_csv(name, university_class, study_time):
    with open(RECORDS_CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, university_class, study_time])
    print("Record saved to CSV.")


def load_records_from_csv():
    records = []
    try:
        with open(RECORDS_CSV_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:  # Ignore empty rows
                    records.append(row)
    except FileNotFoundError:
        print("No study records CSV file found. A new file will be created upon saving.")
    return records


TIME_CSV_FILE = "time_records_file.csv"

def save_time_to_csv(name, university_class, i_time, f_time, total_time):
    with open(TIME_CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, university_class, i_time, f_time, total_time])
    print("Time saved to CSV.")


def load_time_from_csv():
    records = []
    try:
        with open(TIME_CSV_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:  # Ignore empty rows
                    records.append(row)
    except FileNotFoundError:
        print("No time CSV file found. A new file will be created upon saving.")
    return records


#################################################################
# functions

def record_event():
    previous_time = None

    while True:
        # Ask for user's name
        name = input("\nPlease enter your name (or type 'exit' to quit): ")
        if name.lower() == 'exit':
            break

        # Ask for university class
        university_class = input("Please enter the university class: ")

        # Ask for study time
        study_time = input("Please enter the time you took studying for this class (e.g., '2 hours', '30 minutes'): ")

        # Get the current date and time
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

        # Record the event
        save_records_to_csv(name, university_class, study_time)

        print(f"\nEvent recorded successfully at {formatted_time}:\nName: {name}\nClass: {university_class}\nStudy Time: {study_time}\n")


def record_time():
    
    while True:
        # Ask for user's name
        name = input("\nPlease enter your name (or type 'exit' to quit): ")
        if name.lower() == 'exit':
            break
        
        # Ask for university class
        university_class = input("Please enter the university class: ")
        
        # Wait for the user to start recording
        start_input = input("Press Enter to start recording the time, or type 'exit' to quit: ")
        if start_input.lower() == 'exit':
            print("Exiting the time recorder.")
            break

        # Record the start time
        start_time = time.time()
        current_time = datetime.datetime.now()
        i_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"Recording started at {i_time}...")

        # Wait for the user to stop recording
        stop_input = input("Press Enter to stop recording the time: ")
        
        # Record the stop time
        stop_time = time.time()
        current_time = datetime.datetime.now()
        f_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"Recording stopped at {f_time}.")

        # Calculate the time difference
        time_difference_s = stop_time - start_time
        time_difference_m = time_difference_s//60
        time_difference_s = (time_difference_s%60)//1
        print(f"Time recorded: {time_difference_m:.2f} minutes, {time_difference_s:.2f} seconds.")

        save_time_to_csv(name, university_class, i_time, f_time, int(time_difference_m))

        # Ask if the user wants to restart
        restart_input = input("Do you want to record another time interval? (yes/no): ")
        if restart_input.lower() != 'yes':
            print("Exiting the time recorder.")
            break


def show_menu():
    
     while True:
        menu_choice = input(f'\nWelcome. Please choose an option:\n1) Record study time\n2) Record new study event\n3) Exit\n>> ')
        
        if menu_choice == '1':
            record_time()
        
        elif menu_choice == '2':
            record_event()
        
        elif menu_choice == '3':
            break
        
        else:
            print('Invalid option!')
            show_menu()

#################################################################
# main

if __name__ == "__main__":
    study_records = load_records_from_csv()
    time_records = load_time_from_csv()
    
    if study_records:
        print("\nExisting study records:")
        for record in study_records:
            print(record)
    else:
        print("No existing study records found.")
        
    if time_records:
        print("\nExisting time records:")
        for record in time_records:
            print(record)
    else:
        print("No existing time records found.")

    show_menu()
