import unittest
import divisor_master

class MyTestCase(unittest.TestCase):
    def test_prime_number(self):
        self.assertTrue(divisor_master.prime_number(5) == True)

    def test_number_divisors(self):
        assert divisor_master.number_divisors(1.5)

    def test_max_prime_divider(self):
        self.assertTrue(divisor_master.max_prime_divider(100) == [1, 2, 4, 5, 10, 20, 25, 50])


    def test_max_prime_divider(self):
        self.assertTrue(divisor_master.max_prime_divider(10) == 5)


    def test_max_divider(self):
        self.assertTrue(divisor_master.max_divider(20) == 5)



if __name__ == '__main__':
    unittest.main()
