print("Welcome to 'Choose your own Adventure'")
print("You're an adventurer trying to dig up the lost treasure on Treasure Island\n")
print("On the way there, you are faced with a crossroad. Do you turn Left or Right?")
direction = input("l/r:  ")
if direction == "l":
    print("The path leads you to the shore and you can see the Island in the distance. Do you swim across or look "
          "around?")
    decision = input("s/l: ")
    if decision == "s":
        print("You were devoured by some hungry sharks. Try again")
    else:
        print("You come across a broken boat that washed up on the shore. Do you use it to ride across?")
        decision = input("y/n: ")
        if decision == "n":
            print("While looking around, a wild tiger jumped out of a nearby tree and killed you. Try again")
        else:
            print("You make it to the island unharmed. On the island you enter a small house, the only thing on the "
                  "island that stands out. In the house are 3 doors. Red, Yellow and Blue. Which one do you open?")
            door = input("r/y/b: ")
            if door == "r":
                print("You open the door and the ground under you disappears. You died to a booby trap. Try again")
            elif door == "y":
                print("You open the door and inside is Captain Davy Jones who laughs and takes you to his locker. Try "
                      "again")
            else:
                print("You open the door and the room is filled with Treasure! You win!")
else:
    print("The path leads you deep into the forest. Lost, hungry and tired you decide to eat some berries, "
          "the only food you can find. The berries make you extremely sick and a few days later you die from "
          "dehydration. Try again")