import unittest
from app import is_prime, is_even

class TestIsPrime(unittest.TestCase):


    def test_prime_number(self):
        test_cases = [
            {"id": 1, "input": 2, "expected_result": True},
            {"id": 2, "input": 4, "expected_result": False},
            {"id": 3, "input": -1, "expected_result": False},
            {"id": 4, "input": 5, "expected_result": True},
        ]
        for test_case in test_cases:
                result = is_prime(test_case['input'])
                self.assertEqual(result, test_case['expected_result'], f"Test case {test_case['id']} failed")
                
    def test_is_even(self):
        test_cases = [
            {"id": 1, "input": 2, "expected_result": True},
            {"id": 2, "input": -4, "expected_result": True},
            {"id": 3, "input": -1, "expected_result": False},
            {"id": 4, "input": 5, "expected_result": False},
        ]
        for test_case in test_cases:
                result = is_even(test_case['input'])
                self.assertEqual(result, test_case['expected_result'], f"Test case {test_case['id']} failed")

                

if __name__ == '__main__':
    unittest.main()
