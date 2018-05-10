import unittest
from checkPrime import check

DATA_TABLE =[
    {'input': 7, 'expected': True},
    {'input': 10, 'expected': True}
]

class TestPrime(unittest.TestCase):
    def test_check(self):
        for data in DATA_TABLE:
            result = check(data['input'])
            self.assertEqual(result, data['expected'])

if __name__ == '__main__':
    unittest.main()
