def go_sukiya(wallet):
    menu = {
        "牛丼ミニ": 290,
        "牛丼並盛": 350,
        "牛丼中盛": 480
    }

    print("いらっしゃいませ！")
    print("何をご注文なさいますか？")

    product = choice(menu)

    print("承知いたしました")

    if can_pay(wallet, menu[product]):
        wallet = wallet - menu[product]
        print("お釣りは" + str(wallet) + "です")
        print("ありがとうございました！またのご来店をお待ちしております")
    else:
        print("支払えるだけのお金を持っていないようですね")
        wallet = 0
    return wallet


def can_pay(wallet, price):
    if wallet == 0:
        return False
    if wallet - price < 0:
        return False
    return True


def choice(menu):
    print(menu)
    product = input()
    while not product in menu:
        print()
        print("お店にある商品を選んでください")
        print(menu)
        product = input()


if __name__ == "__main__":
    wallet = 1000
    while (True):
        print("現在の所持金:" + str(wallet))
        wallet = go_sukiya(wallet)

        if wallet == 0:
            print("もうすき家にはいけません...")
            break
        else:
            print("もう一度すき家にいきますか？(y/n)")
            is_visit = input()
            if is_visit == "n":
                break
