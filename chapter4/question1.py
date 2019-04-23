def go_sukiya(wallet):
    menu = {
        "牛丼ミニ": 290,
        "牛丼並盛": 350,
        "牛丼中盛": 480
    }

    print("いらっしゃいませ！")
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
