# CMPUT 291 Mini-project 1
# Joe Heppelle: heppelle@ualberta.ca
# Ranajay Sarma: sarma@ualberta.ca

import sqlite3
import random



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

    # TODO: implement type checking etc..
    print("offering ride!")
    date = input("Enter date: ")
    seat_num = input("Enter number of seats: ")
    seat_price = input("Enter price of seat: ")
    lugg_desc = input("Enter luggage description: ")
    source_location = input("Enter source location: ")
    destination = input("Enter destination: ")

    car_number = input("Enter car number: ")
    # TODO: verify car number.

    add_enroute = True
    while add_enroute:
        print("Search for a enroute location. (enter '0' to terminate search.)")
        enroute = input("Enter keyword to search: ")
        if enroute == '0':
            break
        else:
            #TODO 3.1.1: Allow for location code.
            #TODO 3.2.1: if keyword!=location code, display 5 matching locations.
            #TODO 3.2.2: if there are more than 5 matching locations, display 5 at a time
            #TODO 3.2.3: let the member chose out of the matching locations.
            print("Searching for enroute locations...") # test purpose

    rno_generate = True
    while rno_generate:
        rno = random.randint(0,100000)
        # TODO: if rno already exists in database, keep generating new rnoself.
        rno_generate = False                # test purpose

    # TODO 5.0: Set the member as the driver.
    print("Ride offere created!...")

def search_ride(user_email):
    # TODO: implement basic flow of the task
    print("searching for a ride!")
    keywords = []                 # keywords to be searched.
    add_keywords = True
    search = True
    while search:
        while add_keywords:
            keyword = input("Enter a keyword to search for a ride (enter '0' to finish adding keywords): ")
            if keyword = '0':
                break
            keywords.append(keyword)

        # TODO: 1.1.0: Return all rides which match the keywords.
        # TODO: 1.1.1: if keywords match source location, destination, or enroute.
        # TODO: 1.1.2: if city, province, or the address contains keyword as a substring.
        # TODO: 1.2.0: Display all details of the matching rides (from rides table), and car details.
        # TODO: 1.3.0: Display 5 rides at a time.
        # TODO: 1.4.0: Provide options to see more rides if matches >5.

        # TODO: 2.0: Allow user to select a ride from the rides provided.

        # TODO: 3.0: Allow user to send a message to the member posting the ride to book a seat.

        response = input("Make another search?(Y/N): ")
        if response == 'N':
            search = False

def view_booking(user_email):
    # TODO: 1.0: Allow member to list all bookings on rides he offers/
    # TODO: 1.0.0: Allow cancel of any of those bookings.
    # TODO: 1.0.1: Send cancellation message to members who  had booked that ride.
    print("Viewing bookng details...")

def booking(user_email):
    # TODO: implement basic flow of the task
    # TODO: 2.0: Allow members to book rides.
    # TODO:2.0.0: let member select a ride to book.
    # TODO:2.0.1: let member enter his email
    # TODO:2.0.2: let member enter the number of seats booked.
    # TODO:2.0.3: let member enter cost/seat.
    # TODO:2.0.4: let member enter pickup and dropoff location codes.
    # TODO:2.0.6: Display warning if ride is overbooked (number of seats booked>number of seats offered)
        # TODO:2.0.6.1: ask to confirm the overbooked ride.
    # TODO:2.0.7: assign unique bno to the booking made.
    # TODO:2.0.8: send message to member who is offering the ride, that this member is booked on the ride.
    print("Booking a ride...")

def post_ride_request(user_email):
    # TODO: implement basic flow of the task
    date = input("Enter the date of the ride: ")
    pickup_l = input("Enter the pickup location code: ")
    dropoff_l = input("Enter the dropoff location code: ")
    amount_per_seat = input("Enter the amount you are willing to pay per seat: ")

    rid = random.randint(0,10000)
    # TODO: check the rid doesnt exist in database

    # TODO: 3.0: email of the requesting member is the email for the ride.
    print("posting a ride request!")

def show_ride_request(user_email):
    #TODO: 1.0: allow member to see his ride requests
    #TODO: 2.0: allow member to delete any of them.
    print("Showing ride requests")

def search_ride_request(user_email):
    #TODO: 3.0: allow user to search for ride requests with pickup location(code or a city)
    #TODO: 3.1: show 5 matches at a time.
    #TODO: 3.2: allow user to select a request and message the posting member.
    print("Searching for ride requests")

def ride_request(user_email):
    # TODO: implement basic flow of the task
    while (True):
        command = input("Enter 'sh' to view your ride requests, or 's' to search for others ride requests: ")
        if command = '0':
            break
        elif command.lower() = 'sh':
            show_ride_request(user_email)
        elif command.lower() = 's':
            search_ride_request()
        else:
            print("Invalid option...")

    print("searching for a ride request!")

def flow(user_email):
    task = ""
    while (True):
        print("Select a task. 'O' to offer a ride, 'S' to search for a ride, 'book' to book a ride, 'vbook' to view booking details. 'P' to post ride requests, 'SR' for editing and searching ride requests.")
        task = input("Enter task > ")

        if (task.lower() == 'o'):
            offer_ride(user_email)
        elif (task.lower() == 's'):
            search_ride(user_email)
        elif (task.lower() == 'book'):
            booking(user_email)
        elif (task.lower() == 'vbook'):
            view_booking(user_email)
        elif (task.lower() == 'p'):
            post_ride_request(user_email)
        elif (task.lower() == 'sr'):
            ride_request(user_email)
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
    user_email = "joeheppelle123@hotmail.com"
    flow(user_email)

    # conn.commit()
    # conn.close()
main()
    # Log in a user or register a new user.
