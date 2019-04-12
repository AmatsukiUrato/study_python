# coding: utf-8

import random


def main():
    H = random.randint(1, 30)
    W = random.randint(0, 20)
    h = random.randint(1, H)
    w = random.randint(1, W)
    calc1(H, W, h, w)
    calc2(H, W, h, w)


def calc1(H, W, h ,w):
    print(H, W, h, w)

    # 1
    allSell = H * W

    drawH = h * W
    drawW = w * H

    overDraw = h * w
    drawedSell = drawH + drawW - overDraw

    print(allSell, drawH, drawW, overDraw, drawedSell)

    print(allSell - drawedSell)
    return allSell - drawedSell

def calc2(H,W,h,w):
    # 2
    ans = (H - h) * (W - w)
    print(ans)
    return ans



if __name__ == "__main__":
    main()
