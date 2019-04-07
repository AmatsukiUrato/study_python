# coding: utf-8

import random


def main():
    H = random.randint(1, 30)
    W = random.randint(0, 20)
    h = random.randint(1, H)
    w = random.randint(1, W)

    print(H, W, h, w)

    # 1
    allSell = H * W

    drawH = h * W
    drawW = w * H

    overDraw = h * w
    drawedSell = drawH + drawW - overDraw

    print(allSell, drawH, drawW, overDraw, drawedSell)

    print(allSell - drawedSell)

    # 2
    print((H - h) * (W - w))


if __name__ == "__main__":
    main()
