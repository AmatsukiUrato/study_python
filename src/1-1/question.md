# Question
https://atcoder.jp/contests/abc121/tasks/abc121_a
これのa問題をpython3で解く
引数読み込みでランダムは面倒くさいので、下記の様な記述でOK
```python=
# coding: utf-8

import random

H = random.randint(1, 30)
W = random.randint(0, 20)
h = random.randint(1, H)
w = random.randint(1, W)

print(H,W,h,w)
```