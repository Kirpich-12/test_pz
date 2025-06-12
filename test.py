import unittest
from code_1 import sqrt as urv

class TestUrv(unittest.TestCase):
    #Все имена должны наз-ся с test_
    def test_int_pos_num(self):
        self.assertEqual(urv(2, 1), 5.1962)
    def test_int_neg_num(self):
        self.assertEqual(urv(2, -1), 0.3333)
    def test_z_d(self):
        self.assertEqual(urv(2, 2), 'Не дели блет на 0')
    def test_pos_float_num(self):
        self.assertEqual(urv(0.2, 0.1), 1.6432)
    def test_neg_root(self):
        self.assertEqual(urv(1, -2), 'Компл область')
    def test_er_inp(self):
        self.assertEqual(urv('dsadas', '0'), 'А нормально ввести можно было')
        self.assertEqual(urv("", 0), 'А нормально ввести можно было')
        self.assertEqual(urv("10**-9", 'd'), 'А нормально ввести можно было')

if __name__ == '__main__':
    unittest.main()


