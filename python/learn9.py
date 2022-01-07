import unittest
from learn8 import get_name


class Test(unittest.TestCase):
    def test(self):
        name = get_name('tom', 'jack')
        self.assertEqual(name, 'Tom Jack')


if __name__ == '__main__':
    unittest.main()
