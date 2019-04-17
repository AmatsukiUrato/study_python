import unittest
from chapter5 import player


class TestPlayer(unittest.TestCase):

    # テストクラスが初期化される際に一度だけ呼ばれる (python2.7以上)
    @classmethod
    def setUpClass(cls):
        cls.p1 = player.Player("p1", ("say1", "say2"))
        cls.p2 = player.Player("p2", ("say3", "say4"))

    def test_choose_hand(self):
        self.p1.choose_hand()
        self.p2.choose_hand()

        self.assertIn(self.p1.myself_hand_number, [1, 2, 3])
        self.assertIn(self.p2.myself_hand_number, [1, 2, 3])

        # use greater(equal) less(equal)
        self.assertEqual(self.p1.myself_hand_number < 1 or 3 < self.p1.myself_hand_number, False)
        self.assertEqual(self.p1.myself_hand_number < 1 or 3 < self.p2.myself_hand_number, False)

    def test_show_hand(self):
        self.assertIn(self.p1.show_hand(), ["グー", "チョキ", "パー"])
        self.assertIn(self.p2.show_hand(), ["グー", "チョキ", "パー"])


if __name__ == "__main__":
    unittest.main()
