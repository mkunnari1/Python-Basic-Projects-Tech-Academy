"""
python: 3.7.1

Author: Matt Kunnari

Purpose: Tech Academy Training Game,  creating a simple textbased game
"""

def start(nice=0,mean=0,name=""):
   # get user name
   name = describe_game(name)
   nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
    '''
    check if this is a new game or not
    if it is new get the users name
    if not thank the player for playing again and continue
    '''

    if name != "":
        print("\nWelcome back {}! thank you for playing again.".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name adventurer? \n>>>").capitalize()
                if name != "":
                    print("\Welcome, {}!".format(name))
                    print("\n In this game you will be approached by serveral people. \nYou can choose to be nice or mean to them!")
                    print("Remember....... \nAt the end of the game, \nyour fate will bet sealed by your decisions.")
                    stop = False
    return name

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches \nWill you be nice or mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice+1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you menacingly \nthey quickly walk away...")
            mean = (mean+1)
            stop = False
    score(nice,mean,name) # pass the 3 variables into the score()

def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))

def score(nice,mean,name):
    # score function is being passed the values stored within the 3 variables
    if nice > 2: # if condition is valid call win function passing in the variables so it can use them
        win(nice,mean,name)
    if mean > 2:
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    print("Congratulations {} on not being shitty! YOU ROCK!!!".format(name))
    again(nice,mean,name)

def lose(nice,mean,name):
    print("Wow {}, way to be a dick... you should rethink your approach.".format(name))
    again(nice,mean,name)

def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (Y/N): \n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            stop == False
            quit()
        else:
            print("\nEnter (Y) for 'YES' or (N) for 'NO': \n>>> ")

def reset(nice,mean,name):
    nice = 0
    mean = 0
    #be sure not to reset the name variable or else it will ask their name again
    start(nice,mean,name)
    

    
    







if __name__ == "__main__":
    start()
