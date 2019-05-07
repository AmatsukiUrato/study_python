import unittest

from chapter3 import question1


class TestChapter3Question1(unittest.TestCase):
    def test_can_pay(self):
        self.assertEqual(question1.can_pay(1000, 600), True)
        self.assertEqual(question1.can_pay(1000, 1200), False)

    def test_can_pay2(self):
        self.assertEqual(question1.can_pay(0, 600), False)
        self.assertEqual(question1.can_pay(-200, 600), False)


if __name__ == "__main__":
    unittest.main()
