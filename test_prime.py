import unittest
from checkPrime import isPrime 

DATA_TABLE =[
    {'input': -1, 'expected': False},
    {'input':  3, 'expected': True},
    {'input': 10, 'expected': False}
]

class TestPrime(unittest.TestCase):
    # def test_that_3_is_prime(self):
        # expected = True
        # actual = isPrime(3)
        # self.assertEqual(actual, expected)
    # def test_that_10_is_prime(self):
        # expected = True
        # actual = isPrime(10)
        # self.assertEqual(actual, expected)
    def test_check(self):
        actual = False
        for data in DATA_TABLE:
            try:
                actual = isPrime(data['input'])
                self.assertEqual(actual, data['expected'])
            except AssertionError as error:
                print("Input was ", data['input'], "\nExepected value: ",
                      data['expected'], "\nActual Value: ", actual)
                raise Exception(error)

if __name__ == '__main__':
    unittest.main()
