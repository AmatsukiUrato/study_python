from unittest import TestCase
from src.chapter1 import question1


class TestChapter1(TestCase):
    def test_calc1(self):
        self.assertEqual(question1.calc1(3, 2, 2, 1), 1)
        self.assertEqual(question1.calc1(5, 5, 2, 3), 6)


    def test_calc2(self):
        self.assertEqual(question1.calc2(3, 2, 2, 1), 1)
        self.assertEqual(question1.calc2(5, 5, 2, 3), 6)