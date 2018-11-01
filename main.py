# CMPUT 291 Mini-project 1
# Joe Heppelle: heppelle@ualberta.ca
# Ranajay Sarma: sarma@ualberta.ca

import sqlite3


def start():
    user_type = input("Welcome, select 'L' to login or 'S' to signup if you are a new user!")
    if (user_type.lower() == 'l'):
        print("Processing Log In...")
        user_email = input("Please enter your email: ")
        # verify email
        #user_password = input("Please enter your password: ")
        # verify password
        return user_email
    if (user_type.lower() == 's'):
        print("Processing Sign up...")
        new_user_email = input("Please enter sign up email: ")
        # verify email, reprompt if email already exists.
        #new_user_name = input("Please enter your name: ")
        #new_user_phone = input("Please enter your phone number: ")
        #new_user_password = input("Please enter password: ")
        # insert new account information to the database
        print("account created!")
        return new_user_email
    if (user_type == '0'):
        return user_type
    else:
        print("Invalid input!")
        return None

def print_messages(user_email):
    # find new messages to this email.
    # print all messages
    # change statues
    print("New messages while you were gone...")

# this is where the member tasks will be distrubuted
def offer_ride(user_email):
    # TODO: implement basic flow of the task
    print("offering ride!")

def search_ride(user_email):
    # TODO: implement basic flow of the task
    print("searching for a ride!")

def booking(user_email):
    # TODO: implement basic flow of the task
    print("Booking a ride")

def post_ride_request(user_email):
    # TODO: implement basic flow of the task
    print("posting a ride request!")

def search_ride_request(user_email):
    # TODO: implement basic flow of the task
    print("searching for a ride request!")

def flow(user_email):
    task = ""
    while (task != '0'):
        print("Select a task. 'O' to offer a ride, 'S' to search for a ride, 'book' for booking details, 'P' to post ride requests, 'SR' for editing and searching ride requests.")
        task = input("Enter task > ")

        if (task.lower() == 'o'):
            offer_ride(user_email)
        elif (task.lower() == 's'):
            search_ride(user_email)
        elif (task.lower() == 'book'):
            booking(user_email)
        elif (task.lower() == 'p'):
            post_ride_request(user_email)
        elif (task.lower() == 'sr'):
            search_ride_request(user_email)
        elif (task == '0'):
            print("Terminating program...")
            exit()
        else:
            print("invalid request.")

def main():
    '''
    db = 'file_location'
    try:
        conn = sqlite3.connect(sqlite_file)
    except:
        print("Connection to database not established.")
    c = conn.cursor()
    '''

    '''
    user_email = start()
    if (user_email == None):
        print("Invalid email, terminating program...")
        # conn.close()
        exit()
    elif (user_email == '0'):
        print("Terminating program...")
        # conn.close()
        exit()
    else:
        print_messages(user_email)
    '''
    # after login/signup and messages are displayed
    user_email = "joeheppelle123@hotmail"
    flow(user_email)

    # conn.commit()
    # conn.close()
main()
    # Log in a user or register a new user.
