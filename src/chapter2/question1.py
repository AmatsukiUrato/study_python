# coding: utf-8
import time
import random

def main():
    characters = ["RYU", "KEN"]
    my_name = "Player"
    opp_name = "Computer"
    print(my_name + " Turn")
    my_character = choose_character(characters, my_name)
    print(opp_name + " Turn")
    opp_character = choose_character(characters, opp_name)

    my_hp = 100
    opp_hp = 100
    round = 1
    while(True):
        print("==========----------")
        print("ROUND " + str(round))
        print("----------==========")
        time.sleep(0.5)
        print(">>>>>>>>>>>>>>>>>>>>")
        print("READY TO FIGHT")
        print(">>>>>>>>>>>>>>>>>>>>")
        time.sleep(0.5)
        my_atk = random.randint(0, 20)
        opp_atk = random.randint(0, 20)

        my_hp -= opp_atk
        opp_hp -= my_atk
        print( my_name + " HP is " + str(my_hp))
        print( hp_gauge(my_hp))
        print( opp_name + " HP is " + str(opp_hp))
        print( hp_gauge(opp_hp))

        time.sleep(0.1)
        if my_hp <= 0 and opp_hp <= 0:
            print("DRAW")
            break

        if my_hp <= 0:
            print(opp_name + " " + opp_character + " WIN!")
            break

        if opp_hp <= 0:
            print(my_name + " " + my_character + " WIN!")
            break
        round += 1
        print()


def choose_character(characters, player_name):
    print("Please select " + player_name + " character")
    print(characters)
    selected_character = input()
    print("selected: " + selected_character)

    if selected_character in characters:
        return selected_character
    else:
        print("Your select character isn't correct")
        choose_character(characters, player_name)


def hp_gauge(hp_amount):
    hp_gauge = ""

    for i in range(0, hp_amount):
        hp_gauge += "█"
    return hp_gauge


if __name__ == "__main__":
    main()
