#<--------------IMPORT STATEMENTS----------->

from spy_details import Spy,friends

from termcolor import colored

from spy_details import spy

#<--------FUNCTION FOR ADDING A FRIEND------->

def add_friend():

    # Using the class spy

    new_friend = Spy(" ", " ", 0, 0.0)

    new_friend.name = raw_input("Please add your friend's name: ")

    new_friend.salutation = raw_input("Are they Mr. or Ms. ?: ")



    # ask for the age of the friend

    new_friend.age = raw_input("Age?: ")

    # Type casting to integer

    new_friend.age = int(new_friend.age)



    # Ask for the rating of the friend

    new_friend.rating = raw_input("Spy rating?: ")

    # Type casting to float

    new_friend.rating = float(new_friend.rating)



    # Add a friend of correct age and equal or higher rating

    # Valid name of strings must be entered

    if (len(new_friend.name) > 0 and new_friend.name.isdigit() == False and 12 < new_friend.age < 50 ):

        if (new_friend.salutation== 'ms.' or new_friend.salutation=='Ms.'or new_friend.salutation=="Mr."or new_friend.salutation=="mr."):





            # After the conditions are satisfied the friend will be added

            friends.append(new_friend)

            print(colored('Friend Added!', "green"))

        else:

            print(colored("NO FRIEND ADDED..!!.Salutation input error...WRITE(Ms./Mr./ms./mr.)", "red"))



        # The no of friends the spy has will be returned.

        return len(friends)

    else:

        print(colored("Sorry NO FRIEND ADDED ,input spy details are wrong", "red"))



    # The no of friends the spy has will be returned.

    return len(friends)