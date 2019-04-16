# coding: utf-8
import random

# PyCharmではfromを正確に書かなければ`No module`になる(sourceFileの中にあるファイルは普通にインポートできる)
# from src.chapter3.component.player import Player
from chapter5.component.player import Player

junken_pattern = {
    "winner_1p_pattern": [("グー", "チョキ"), ("チョキ", "パー"), ("パー", "グー")],
    "winner_2p_pattern": [("チョキ", "グー"), ("パー", "チョキ"), ("グー", "パー")],
    "draw_pattern": [("グー", "グー"), ("チョキ", "チョキ"), ("パー", "パー")],
}


def main():
    myself = Player("エドモンド本田", ("ガッーハッハッハッ！", "お前さん、中々じゃった！", "どんなもんじゃい！", "豪快に決めたでごわす！", "世界は広いのう！"))
    opponent = Player("ガイル", ("Mission Complete", "Easy Operation", "拍子抜けだな", "Good Job"))
    myself.choose_hand()
    opponent.choose_hand()

    myself.say_hand()
    opponent.say_hand()

    janken_judge(myself, opponent)


def janken_judge(myself, opponent):
    janken_result = (myself.show_hand(), opponent.show_hand())

    if janken_result in junken_pattern["winner_1p_pattern"]:
        myself.say_win_voice()
    elif janken_result in junken_pattern["winner_2p_pattern"]:
        opponent.say_win_voice()
    elif janken_result in junken_pattern["draw_pattern"]:
        print("draw")
    else:
        print("error")


if __name__ == "__main__":
    main()
