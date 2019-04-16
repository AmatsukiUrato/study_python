import unittest

from chapter3 import question1
from chapter3 import question2
from chapter3 import question3


class TestChapter3Question1(unittest.TestCase):
    def test_can_pay(self):
        self.assertEqual(question1.can_pay(1000, 600), True)
        self.assertEqual(question1.can_pay(1000, 1200), False)

    def test_can_pay2(self):
        self.assertEqual(question1.can_pay(0, 600), False)
        self.assertEqual(question1.can_pay(-200, 600), False)


class TestChapter3Question2(unittest.TestCase):
    def test_can_pay(self):
        self.assertEqual(question2.can_pay(1000, 600), True)
        self.assertEqual(question2.can_pay(1000, 1200), False)

    def test_can_pay2(self):
        self.assertEqual(question2.can_pay(0, 600), False)
        self.assertEqual(question2.can_pay(-200, 600), False)


class TestChapter3Question3(unittest.TestCase):
    def test_can_pay(self):
        self.assertEqual(question3.can_pay(1000, 600), True)
        self.assertEqual(question3.can_pay(1000, 1200), False)

    def test_can_pay2(self):
        self.assertEqual(question3.can_pay(0, 600), False)
        self.assertEqual(question3.can_pay(-200, 600), False)
