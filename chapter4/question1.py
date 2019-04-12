# coding: utf-8
import random
# PyCharmではfromを正確に書かなければ`No module`になる(sourceFileの中にあるファイルは普通にインポートできる)
# from src.chapter3.component.player import Player
from player import Player


def main():
    myself = Player(name="エドモンド本田")

    myself.chooseHand()
    opponent.test("hoge")


    my_hand = int(input())
    opponent_hand = random.randint(1, 3)

    print("自分の手:" + hand_name(my_hand))
    print("相手の手:" + hand_name(opponent_hand))

    if my_hand == opponent_hand:
        print("draw")
    elif (my_hand == 1 and opponent_hand == 2 or
          my_hand == 2 and opponent_hand == 3 or
          my_hand == 3 and opponent_hand == 1):
        print("win")
    else:
        print("lose")


def hand_name(hand_num):
    hand_str = ""
    if hand_num == 1:
        hand_str = "グー"
    elif hand_num == 2:
        hand_str = "チョキ"
    elif hand_num == 3:
        hand_str = "パー"
    else:
        pass
    return hand_str


if __name__ == "__main__":
    main()
