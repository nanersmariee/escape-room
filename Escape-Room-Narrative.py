# Adventure Game: Escape Room


#create a list of movies 
movies_in_library = {"0 - Clueless": 0, "1 - Zombieland": 1, "2 - Titanic": 2, "3 - Superman": 3}
items = []

def intro ():
    """intro, seeing man on tv"""

    print()
    print("Early on a Sunday morning in San Francisco, you wake up in a strange room, with nothing but a bed and a TV.  You step closer towards the TV and notice that it's fuzzy from some sort of bad connection.  You bang on its side until a man appears.  He seems to be looking right at you! He asks,")
    print()
    
    while True:
        
        see_man_response = input("Can you see me? (Y/N) > ").upper()
        
        if see_man_response == "Y":
            print("Wonderful!")
            print()
            break
        
        elif see_man_response == "N":
            print("Yes you can! I'm right here!")
            print()
            break
        
        else:
                print("Not a valid response, try again.")

def will_you_help_me():
    """ Will you help him?"""
    while True:
        get_help = input("Do you want to play a game? (Y/N)> ").upper()
        
        if get_help == "Y":
            print("That's amazing!  Close your eyes and take a deep breath! ")
            break
                
        elif get_help == "N":
            print("Too bad!  You have no choice, you're going to play! ")
            print()
            break
                
        else:
            print("Not a valid response, try again. ")
            print()
            print()
            break
    print("You get a little light headed and notice the channel flickering.  You suddenly feel yourself getting sucked into the TV!")
    print()

#BASIC RULES OF THE GAME/OBJECT OF THE GAME

def rules_of_game():
    """basic rules of the game"""

    name = input("You come face to face with the mysterious man. He says, 'My name is 'Doc' and I'm your TV Guide. What's your name? > ").title()
    print("Nice to meet you {}!".format(name))
    
    print()
    print("There are four channels on this TV, each playing a different movie.  Each movie will hold a clue to get you one step closer to escape.  Your goal is to ESCAPE THE TV!  Do you have the wit to answer all the trivia questions?")
    return name
    # You have to navigate through movies to escape.  But you have to find him, he's not sure which movie he's stuck in!

def movie_library():
    """iterates over movies"""

    for movie in (movies_in_library):
        print(movie)
        
def clueless():
    """Clueless Trivia is Activated"""

    
    print()
    
    print("A woman approaches, 'Hi, I'm Cher.' I have a question: ")

    
    
    while True:
        answer = input("""What is the best way to spend a Friday night?
        
        [A] - Doing Homework
        [B] - Going to the Gym
        [C] - Doing Makeovers
        
        > """).upper()
        
        
        if answer == "A":
            print("Ugh! As if!! Try Again!")
            
        elif answer == "B":
            print("Ugh! As if!! Try Again!")
        
        elif answer == "C":
            
            print("You're like totally right!")
            break
        
        else:
            print("Whatever! That totally isn't even an option, try again. Don't be a Loser")
    
    print("Who even likes Homework? See look, I'm failing Debate class.  You seem smart, maybe you'll have better luck.  Take this. ")
    print()
    print("ITEM OBTAINED: Test with a big fat 'F' ")
    
    print()
    
    items.append("F")
    del movies_in_library ["0 - Clueless"]
    
    #return items??

def zombieland():
    """Zombieland Trivia is activated"""

    
    print()
    print("You open your eyes and are in chaos.  You are crouched behind a sofa as two zombies crawl in from the side window. 'Get down!' a man screams and hands you a shotgun. 'I'll take the one on the left, you take the one on the right' ")
    
   

    while True:
        answer = input("""Where do you aim to shoot?
        
        [A] - Zombie's Chest
        [B] - Zombie's Head
        [C] - Zombie's Legs
        
        > """).upper()
        
        
        if answer == "A":
            print("Oh no!  He's still coming after you! Try Again")
            
        elif answer == "C":
            print("Oh no!  He's still coming after you! Try Again")
        
        elif answer == "B":
            
            print("The Zombie goes down!")
            break
        
        else:
            print("You can't aim there! Try again from the list of options.")
    
    print("You look over ready to give the man a high five but in the corner of your eye, still see the Zombie coming back up! 'Don't be stingy with bullets' always double tap.' You shoot the Zombie in the head again! An eye pops out, and the man pops it into your shirt pocket.  Hold on to it for safekeeping.")

    print()
    print("ITEM OBTAINED: an EYE ")
    
    print()
    
    items.append("EYE")
    del movies_in_library ["1 - Zombieland"]


def titanic():
    """Titanic Trivia is activated"""

    
    print()
    
    print("Suddenly you find yourself on a ship in the middle of the ocean.  It hard to make out, but it appears there's a woman standing on a railing at the end of a ship. She says, 'Don't come any closer!' Afraid that she might take a plunge: ")
    
    

    while True:
        answer = input("""What do you say?
        
        [A] - Don't jump!
        [B] - I'm the king of the world!  
        [C] - I'm going to call the police!
        
        > """).upper()
        
        
        if answer == "A" or answer == "C":
            print("She ignores you, Try Again!")
            
        elif answer == "B":
            
            print("She says, 'I once knew someone who liked to say that.'")
            break
        
        # elif answer == "C":
        #     print("She ignores you, Try Again!")
        
        else:
            print("Huh? I don't understand, Try Again.")
    
    print("'He was my old beau, the love of my life, Jack.' She turns around and you realize it's actually an old woman speaking to you. She continues, 'I was going to toss this.  You go ahead and have it.' She hands you a necklace.")
    
    print()
    print("ITEM OBTAINED: HEART of the ocean ")

    print()
    
    items.append("HEART")
    del movies_in_library ["2 - Titanic"]
    
def superman():
    """Superman Trivia is activated"""

    
    print()
    
    print("You feel yourself falling in the sky, but in one quick swoop, you're on a rooftop. Up in the sky, you see something zip by.")
    


    while True:
        answer = input("""What is it?
        
        [A] - It's a bird
        [B] - It's a plane
        [C] - It's Superman 
        
        > """).upper()
        
        
        if answer == "A":
            print("Too big to be a bird! Try Again!")
            
        elif answer == "B":
            print("Too small to be a plane!  Try Again!")
        
        elif answer == "C":
            
            print("As you say Superman, he appears at your side. 'Yup it's me kid. Always strive to help the greater good.  Here, a symbol of Truth, Justice, and the American way.")
            break
        
        else:
            print("Huh? I don't understand, Try Again.")
    
    print("He hands you a replica of his suit and cape.")
    print()
    print("ITEM OBTAINED: Suit with an S ")
    print()
    
    items.append("S")
    
    del movies_in_library ["3 - Superman"]

def enter_movie():
    """Entering each movie, user can select which movie to enter"""
    # Movie 1
    #Trivia questions to "beat the movie"
    #If answers correctly, get awarded an item
    #Item gets added to the player's list
    #Erase movie from list of options

    while True:
        selected_movie = input("Indicate which movie that you would like to visit by entering the corresponding channel. ")
        print()

        if selected_movie == "0":
            print("You are now entering CLUELESS")
            clueless()
            break
        
        elif selected_movie == "1":
            print("You are now entering ZOMBIELAND")
            zombieland()
            break
            
        elif selected_movie == "2":
            print("You are now entering TITANIC")
            titanic()
            break
            
        elif selected_movie == "3":
            print("You are now entering SUPERMAN")
            superman()
            break 
        
        else:
            print("Invalid choice, try again.")
            print()

def solve_puzzle():
    """Solving Final Puzzle to escape"""
    #If players obtains all 4 items, leads them to final puzzlet

    
    print("You have obtained all 4 items, which serve as clues to the final passcode!  Each item is attached to a specific number, but what's the correct combination?")
    
    print()
    
    while True:
        #Associate each item to an index
        completed_item_list = ["HEART", "EYE", "F", "S"]
        for i, item in enumerate(completed_item_list):
            print(i, item)
            
        print()
        #hey must crack thh final code of the remote control
        answer = input("What code do you punch into the remote control to escape? ")
   
        #The correct number combination saves them from the TV trap and they've escaped!
        if answer == "1032":
           
            print("""1032 is correct!  
            
            You solved the code
            
            EYE
            HEART
            S 
            F 
            
            CONGRATULATIONS {}
            
            Doc reappears to shake your hand, except now he is in life form!  You look over and the TV now has a crack down the middle of the screen with smoke coming out of the sides.  You are back in the room and Doc exclaims, 'We are free!!'

            You have escaped the TV!""".format(player_name)) 
            break
        
        else:
            print()
            print("Incorrect, please try again")
            print("HINT: What is the best city in the world?")
            print()

        #WINNING condition
        #If they answer all trivia questions, and make it to the end AND solve the final passcode

def game_play():
    """Create list of options: main game play, main loop to enter movie, view item, or quit"""

    options = ["[E]nter Movie", "[V]iew Items", "[Q]uit"]
    print()
    
    while True:
        
        if "F" in items and "EYE" in items and "HEART" in items and "S" in items:
            
            solve_puzzle()
            break
        
        print()
        for option in options:
            print(option)
        print()    
    
        selected_option = input("Please select from the list of options > ").upper()
        print()
        
        if selected_option == "E":
            movie_library()
            print()
            enter_movie()
        
        elif selected_option == "V":
            print("You are currently holding:")
            for item in items:
                print(item)
            print()
            
        elif selected_option == "Q":
            print("Oh no!  You'll be trapped here forever!")
            print("GOODBYE")
            break
           
        else:
            print("Not a valid option, try again. ")

intro()    
will_you_help_me()
player_name = rules_of_game()
game_play()