# coding: utf-8
import random


def main():
    characters = ["RYU", "KEN"]
    print(choose_character(characters))
    print("end")

    # print("Please type enemy's character")
    # print(character)
    # oppCharacter = input()
    #
    # if not myCharacter in characters:
    #
    # for character in characters:
    #     if


def choose_character(characters):
    print("Please select character")
    print(characters)
    selected_character = input()
    print("selected: " + selected_character)

    if selected_character in characters:
        return selected_character
    else:
        print("Your select character isn't correct")
        choose_character(characters)


if __name__ == "__main__":
    main()
