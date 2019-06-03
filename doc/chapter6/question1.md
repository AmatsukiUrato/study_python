## 課題6-1
課題1-2で作成したじゃんけんプログラムを
オブジェクト指向ライクに書き直す。

- player.pyのファイル内にPlayerクラスを作成する
- Playerクラスの仕様は以下である
```python
class Player:
    _hand_dictionary = {1: "グー", 2:"チョキ", 3:"パー"}
    def __init__(self, name, winner_sentence):
        pass # 記述する
            
    def choose_hand(self):
        pass # 記述する

    def say_win_voice(self):
        pass # 記述する
        
    def show_hand(self):
        pass # 記述する
        # return
        
    def say_hand(self):
        pass # 記述する
```
- question1.pyから、Playerクラスのインスタンス化を行う
- 出力結果と同じになっているかを確認する

## 出力結果
自分が勝つとき
```text
エドモンド本田の手はグー
ガイルの手はチョキ

エドモンド本田 Win!
ガッーハッハッハッ！
````
相手が勝つとき
```text
エドモンド本田の手はパー
ガイルの手はチョキ

ガイル Win!
Mission Complete
```
引き分け
```text
エドモンド本田の手はチョキ
ガイルの手はチョキ

draw
```
