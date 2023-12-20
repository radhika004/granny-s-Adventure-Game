import time

def introduction():
    print("Welcome to Maggie's Escape Adventure!")
    print("You are Maggie, and your car has broken down on your way to Ladakh.")
    print("You seek help and find a mysterious house. Little do you know, it's haunted!")
    print("Can you escape Granny's house alive?\n")
    print("Granny gonna aske you 10 mystery questions and you have to answer all of them correctly")

def ask_question(question, options):
    print(question)
    for i, option in enumerate(options,1):
        print(f"{i}. {option}")
    
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    
    
def escape_game():
    score = 0
    attempts = 1

    # Introduction
    introduction()

    # Scene 1
    print("\n You enter the house and see a dimly lit hallway.")
    time.sleep(1)
    print("Suddenly, a mysterious voice echoes, 'Welcome, Maggie. To escape, you must answer my questions.'")

    # Question 1
    time.sleep(1)
    answer1 = ask_question("I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?",["echo","phone","watch"])
    if answer1 == 1:
        print("Correct! You may proceed.")
        score += 1
    else:
        print("Incorrect! Granny's ghost appears and kill you.")
        print(" Restart the game")
        
        escape_game()
        

    # Question 2
    time.sleep(1)
    answer2= ask_question("The more you take, the more you leave behind. What am I?", ["footsteps","water","sand"])

    if answer2== 1:
        print("Correct! Granny's ghost seems pleased.")
        score += 1
        
    
    else:
        print("Incorrect! Granny's ghost appears and kill you.")
        print("Restart the game")
        escape_game()
    
        
        
        
    # Question 3
    time.sleep(1)
    answer3= ask_question("What mythical creature is often associated with granting wishes?",["Griffin","Genie","Goblin"])
    if answer3== 2:
        print("Correct! Granny get happy and starts screaming ")
        score += 1
    else:
        print("Incorrect!Granny gonna punish you ")
        print("Restart the game")
        escape_game()
        
        
        
    
    # Question 4
    time.sleep(1)
    answer4= ask_question("Which ancient civilization built the mysterious Stonehenge?",["Egyptians","Romans","Druids"])
    if answer4== 3:
        print("Granny surprised by your knowledge and give the key of store room")
        score += 1
    else:
        print("Incorrect!Granny got angry and locked you in store room")
        print("Restart the game")
        escape_game()
        
        
        
    # Question 5
    time.sleep(1)
    answer5= ask_question("If all cats can fly, and Fluffy is a cat, what can you logically conclude?",[" Fluffy can fly"," Fluffy cannot fly","Some cats can fly"])
    if answer5== 1:
        print("Right answer!!! Granny help you to find store room and enter in it")    
        score += 1
    else:
        print(" This time Granny gonna kill you ") 
        print("Restart the game")
        escape_game()
        
        
        
    # Question 6
    time.sleep(1)
    answer6= ask_question("All roses in Mary's garden are red. If a flower is red, can you conclude it is in Mary's garden?",["Yes","No"," Not necessarily"])
    if answer6== 3:
        print('''Granny jumped with the joy
                She gives you a talking doll who knows the exit 
                You start to follow the doll 
                Granny continues asking questions''')
        score += 1
    else:
        print("You are gonna stuck in the store room for forever")
        print("Restart the game")
        escape_game()
        
        
        
    # Question 7
    time.sleep(1)
    answer7= ask_question("I am a restless spirit seeking peace. I died tragically in this haunted mansion. Who am I?",["Granny herself","The Gardener's Ghost"," The Lost Butler"])
    if answer7== 1:
        print("Granny give you a magical sword to fight with upcoming monster")
        score += 1
    else:
        print("Granny leaves you in hands of monster ")
        print("Restart the game")
        escape_game()
    
        
    # Question 8
    time.sleep(1)
    answer8= ask_question("I am a ghostly figure that appears only at midnight. Who am I?",["Midnight Specter","Phantom Moonlight","The Ghostly Hourglass"])
    if answer8== 1:
        print("Granny helped you to kill the monster")
        score += 1
    else:
        print("Monster kills you")
        print("Restart the game")
        escape_game()
        
        
    #  Question 9
    time.sleep(1)
    answer9= ask_question("I am taken from a mine, and shut up in a wooden case, from which I am never released, and yet I am used by almost every person",["Pencil lead","eraser","Sharpner"])
    if answer9== 1:
        print("You find the escape")
        score += 1
    else:
        print("You gonna stay with Granny for forever")
        print("Restart the game")
        
        escape_game()
        
        
        
    #  Question 10 
    
    time.sleep(1)
    answer10 = ask_question("I fly without wings, I cry without eyes",["baby","cloud","bike"])
    if answer10 == 2:
        print("Granny will repair you car and say GOOD BYE")
        score += 1
    else :
        print("Granny not let you reach to the exit ")
        print("Restart the game")
        escape_game()
        
    
    


    
    print("\nYou reach the exit and see the door to freedom.")
    time.sleep(1)
    print(f"Congratulations, Maggie! You successfully answered {score} out of 10 questions.")
    print("You open the door, rush out, and escape Granny's haunted house!")

if __name__ == "__main__":
    escape_game()

