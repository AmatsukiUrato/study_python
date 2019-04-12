# 課題2-1
1. ユーザにキャラクターを選択させる
2. 相手(CPU)のキャラクターを選択させる
    - キャラクターは配列で定義する
    - キャラクターは[RYU, KEN]とする
3. 選択が終わると対戦が開始される
4. RYUとKENがターン毎に攻撃を行い、最後まで生きていたほうが勝利する
    - 攻撃は0~20ダメージのランダム
    - 一つのターンで両方のキャラが死んだ場合は引き分け
5. 試合が終わればどちらが勝利したかを表示して終了する。

サンプル
```text
Player Turn
Please select Player character
['RYU', 'KEN']
RYU
selected: RYU
Computer Turn
Please select Computer character
['RYU', 'KEN']
KEN
selected: KEN
==========----------
ROUND 1
----------==========
>>>>>>>>>>>>>>>>>>>>
READY TO FIGHT
>>>>>>>>>>>>>>>>>>>>
Player HP is 86
Computer HP is 81

...長過ぎるため省略...

==========----------
ROUND 10
----------==========
>>>>>>>>>>>>>>>>>>>>
READY TO FIGHT
>>>>>>>>>>>>>>>>>>>>
Player HP is 19
Computer HP is -8
Player WIN!
```
ゲージ追加
```text
==========----------
ROUND 7
----------==========
>>>>>>>>>>>>>>>>>>>>
READY TO FIGHT
>>>>>>>>>>>>>>>>>>>>
Player HP is 16
■■■■■■■■■■■■■■■■
Computer HP is 20
■■■■■■■■■■■■■■■■■■■■

==========----------
ROUND 8
----------==========
>>>>>>>>>>>>>>>>>>>>
READY TO FIGHT
>>>>>>>>>>>>>>>>>>>>
Player HP is -2

Computer HP is 19
■■■■■■■■■■■■■■■■■■■
Computer WIN!
```