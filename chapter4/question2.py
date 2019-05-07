import sys
import time


def go_sukiya(wallet, is_bilk):
    menu = {
        "牛丼ミニ": 290,
        "牛丼並盛": 350,
        "牛丼中盛": 480
    }

    print("いらっしゃいませ！")
    if is_bilk:
        print("お客様は一度食い逃げしています")
        print("警察を呼びます")
        sys.exit()

    print("何をご注文なさいますか？")

    products = choice_multiple(menu)

    price = 0
    for product in products:
        price += menu[product]

    if can_pay(wallet, price):
        wallet = wallet - price
        print("お釣りは" + str(wallet) + "です")
        print("ありがとうございました！またのご来店をお待ちしております")
    else:
        print("支払えるだけのお金を持っていないようですね")
        print("・・・どうする？(1 or 2)\n1. 食い逃げする\n2. 皿洗いする")
        while(True):
            action_number = input()
            if action_number == "1":
                print("食い逃げしてしまった")
                print("もう店にはいけない")
                is_bilk = True
                break
            elif action_number == "2":
                wallet = wallet - price
                print("皿洗いをします")
                print("足りないお金分(" + str(abs(wallet)) +")働きます。")
                while(wallet < 0):
                    time.sleep(0.5)
                    wallet += 50
                    print("現在の負債は" + str(abs(wallet)) + "円です")
                print("お疲れ様でした")
                break
            else:
                print("どちらか選んでください(1 or 2)")
    return wallet, is_bilk


def can_pay(wallet, price):
    if wallet == 0:
        return False
    if wallet - price < 0:
        return False
    return True


def choice(menu):
    print(menu)
    product = input()
    if not product in menu:
        print()
        print("お店にある商品を選んでください")
        product = choice(menu)
    return product


def choice_multiple(menu):
    products = []
    while (True):
        products.append(choice(menu))
        print("他にも注文しますか？(y/n)")
        want_buy_again = input()
        if not want_buy_again == "y":
            break
    return products


if __name__ == "__main__":
    wallet = 1000
    is_bilk = False
    while (True):
        print("現在の所持金:" + str(wallet))
        wallet, is_bilk  = go_sukiya(wallet, is_bilk)

        if wallet == 0:
            print("もうすき家にはいけません...")
            break
        else:
            print("もう一度すき家にいきますか？(y/n)")
            is_visit = input()
            if is_visit == "n":
                break
