import time
import random

# Function to introduce the game
def introduction():
    print("Welcome to The Quest for the Lost Amulet!")
    print("You wake up in a small room with stone walls. A dim torch flickers on the wall, casting shadows across the room.")
    print("You have no memory of how you got here, but you feel a sense of purpose stirring within you.")
    print("You must retrieve the Lost Amulet, a powerful artifact stolen by the vile sorcerer, Mahmud, to restore peace to the kingdom.")
    print("Are you ready to embark on your quest?\n")

# Function to combat

def final():
    print("IMPOSSIBLE!")
    print(f"You hit Mahmud with your fist, directly to his head! Mahmud dies and you retrieve the Amulet!")
    time.sleep(3)
    print("But something is wrong...")
    time.sleep(3)
    print("The Amulet glow so bright...")
    time.sleep(3)
    print("You hear a voice in your head...")
    time.sleep(3)
    print("Mysterious voice: You Manage to take it from him? Good...")
    time.sleep(3)
    print("Mysterious voice: Now I have to do this myself!!")
    time.sleep(10)
    print("GOD OF THE AMULET HAS AWOKEN!!!")
    war("God of The Amulet", 1000, 50)

def war(enemyName, enemyHealth, playerHealth):
    while enemyHealth > 0 and playerHealth > 0:
        print("The battle is still running...")
        print(f"Your health: {playerHealth}")
        print(f"{enemyName}'s health: {enemyHealth}")
        act = input("1.Attack or 2.Heal? ")
        if act == "1":
            playerDamage = random.randint(5, 10)
            enemyHealth -= playerDamage
            print(f"You attack {enemyName} with {playerDamage} damage!")
            enemyDamage = random.randint(5, 15)
            playerHealth -= enemyDamage
            print(f"{enemyName} attack you with {enemyDamage}!")
        elif act == "2":
            heal = random.randint(5, 20)
            playerHealth += heal
            print(f"You heal for {heal} life!")
            enemyDamage = random.randint(5, 15)
            playerHealth -= enemyDamage
            print(f"{enemyName} attack you with {enemyDamage}!")
        else:
            enemyDamage = random.randint(5, 15)
            playerHealth -= enemyDamage
            print(f"{enemyName} attack you with {enemyDamage}!")
    if playerHealth <= 0:
        print(f"{enemyName} killed you! Wait 60 seconds to respawn!")
        time.sleep(60)
        print("You respawned!")
        main()
    if enemyHealth <= 0:
        if enemyName == "Mahmud":
            final()
        print("Amazing...")
        print(f"You defeated {enemyName}!")
        time.sleep(5)
        print(f"The God explode, his remains turn back into the Amulet! The kingdom is now in peace, with you as the new prince!")
        print("Wait a minute to play again!")
        time.sleep(60)
        main()
            

def combat(enemyName):
    answer = random.randint(1,5)
    myAnswer = input("Choose from 1 to 5: ")
    if int(myAnswer) == answer:
        print(f"You defeat the {enemyName}!")
        choose_location()
    else:
        print(f"You attack {myAnswer}, {enemyName} attack dodge to {answer}. {enemyName} defeated you! Wait 3 seconds to respawn.")
        time.sleep(3)
        print("You respawned!")
        main()

def boss():
    print("Face my wrath!")
    answer = random.randint(1, 5)
    myAnswer = input("Choose from 1 to 5: ")
    if int(myAnswer) == answer:
        print("Don't feel proud, its not over yet!")
        print(f"You hit Mahmud with your magic!")
        boss2()
    else:
        print("Too weak, kid!")
        print(f"You choose {myAnswer}, Mahmud defeated you with laser beam at {answer}! Wait 10 seconds to respawn.")
        time.sleep(10)
        print("You respawned!")
        main()

def boss2():
    print("Ouch! That hurt!")
    answer = random.randint(1, 10)
    myAnswer = input("Choose from 1 to 10: ")
    if int(myAnswer) == answer:
        print("AAGHH!")
        print(f"You hit Mahmud with your sword!")
        boss3()
    else:
        print("Not bad, but still not enough to defeat me!")
        print(f"You choose {myAnswer}, Mahmud defeated you with the Sword of the Tyrant at {answer}! Wait 20 seconds to respawn.")
        time.sleep(20)
        print("You respawned!")
        main()

def boss3():
    print("How dare you... RRRAAAA!!!")
    answer = random.randint(1, 15)
    myAnswer = input("Choose from 1 to 15: ")
    if int(myAnswer) == answer:
        print("IMPOSSIBLE!")
        print(f"You hit Mahmud with your fist, directly to his head! Mahmud dies and you retrieve the Amulet! The kingdom is now in peace, with you as the new prince!")
        print("Wait a minute to play again!")
        time.sleep(60)
    else:
        print("Marvelous! I shall reward you with a long and painful death!")
        print(f"You throw your final attack at {myAnswer}, but Mahmud defeated you with the Moon's Wrath at {answer}! You were so close, but you failed. Wait 60 seconds to respawn.")
        time.sleep(60)
        print("You respawned! Your body still feel tired, but you decide to push forward and try again.")
        main()

# Function to prompt user for next action
def choose_location():
    print("Choose your next location:")
    print("1. Dark Forest")
    print("2. Haunted Castle")
    print("3. Mystic Caves")
    print("4. Tower of Mahmud")
    choice = input("Enter the number of your choice: ")
    return int(choice)


# Function for Dark Forest location
def dark_forest():
    print("\nYou enter the Dark Forest. The trees loom overhead, and strange noises echo around you.")
    print("You hear a growl nearby. Do you:")
    print("1. Investigate the growl")
    print("2. Ignore it and continue deeper into the forest")
    choice = input("Enter the number of your choice: ")
    if choice == "1":
        print("\nYou cautiously approach the source of the growl...")
        time.sleep(2)
        print("It's a hungry wolf!")
        print("You have no choice but to fight.")
        combat("Wolf")
    elif choice == "2":
        print("\nYou decide to ignore the growl and press on deeper into the forest...")
        print("Wait 5 seconds to get out of the forest.")
        time.sleep(5)
        main()


# Function for Haunted Castle location
def haunted_castle():
    print("\nYou arrive at the Haunted Castle. It looms ominously before you, its dark silhouette against the moonlit sky.")
    print("You feel the air getting colder around you. Do you:")
    print("1. Investigate")
    print("2. Run away")
    choice = input("Enter the number of your choice: ")
    if choice == "1":
        print("\nYou begin investigating the castle...")
        time.sleep(2)
        print("It's an Undead Knight!")
        print("You have no choice but to fight.")
        combat("Undead Knight")
    elif choice == "2":
        print("\nAs you run away, you feel like a loser...")
        print("Wait 5 seconds to get out of the Haunted Castle.")
        time.sleep(5)
        main()


# Function for Mystic Caves location
def mystic_caves():
    print("\nYou venture into the Mystic Caves. The air is thick with magic, and strange symbols adorn the walls.")
    print("You hear a slippery sound nearby. Do you:")
    print("1. Investigate the sound")
    print("2. Ignore it and collect some mana mushroom")
    choice = input("Enter the number of your choice: ")
    if choice == "1":
        print("\nYou cautiously approach the source of the sound...")
        time.sleep(2)
        print("It's a Mystic Lizard!")
        print("You have no choice but to fight.")
        combat("Mystic Lizard")
    elif choice == "2":
        print("\nUnfortunately, the fruit is untouchable. So, you decide to leave...")
        print("Wait 5 seconds to get out of the Mystic Cave.")
        time.sleep(5)
        main()

# Function for Tower of Mahmud location
def tower_of_zardor():
    print("\nYou stand before the Tower of Mahmud, the final bastion of the sorcerer's power.")
    fight = input("I have been waiting for you... Are you ready to die? (Yes or No) ")
    if fight == "Yes":
        print("Good... Now, let the battle begin!")
        war("Mahmud", 150, 100)
    else:
        print("Seriously? I'm not here to give you a cookie, go away!")
        main()

# Main function to run the game
def main():
    location = choose_location()

    if location == 1:
        dark_forest()
    elif location == 2:
        haunted_castle()
    elif location == 3:
        mystic_caves()
    elif location == 4:
        tower_of_zardor()
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

# Run the game
if __name__ == "__main__":
    introduction()
    main()
