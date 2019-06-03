# coding: utf-8


class Hamburger_shop(object):
    def __init__(self, place):
        self.place = place
        self.products = ["ポテト", "ハンバーガー", "チーズバーガー", "ベーコンレタスバーガー", "テリヤキバーガー"]

    def show_product(self):
        print(self.products)

    def show_place(self):
        print(self.place)

    def move_place(self, place, test):
        self.place = place
        self.test = test


class Macdnard(Hamburger_shop):
    def __init__(self, place, original_products):
        # Point
        # super() == super(Macdnard, self)
        super().__init__(place)
        self.products.extend(original_products)

    def move_place(self):
        self.place = "島根店"


class Mos(Hamburger_shop):
    pass


if __name__ == "__main__":
    Hamburger_shop = Hamburger_shop("大阪店")
    Hamburger_shop.show_product()

    macdnard = Macdnard("奈良店", ["バベチ", "バベポ"])
    macdnard.show_product()
    macdnard.show_place()
    macdnard.move_place()
    macdnard.show_place()

    print()
    mos = Mos("東京店")
    mos.show_product()
    mos.show_place()
