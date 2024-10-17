from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testCases = {
            1: ([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]], [20,24]),
            2: ([[1,2,3],[1,2,3],[1,2,3]], [1,1])
        }
        self.__obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_Case1(self):
        nums, output = self.__testCases[1]
        result = self.__obj.smallestRange(nums = nums)
        self.assertIsInstance(result, list)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case2(self):
        nums, output = self.__testCases[2]
        result = self.__obj.smallestRange(nums = nums)
        self.assertIsInstance(result, list)
        self.assertEqual(result, output) 

if __name__ == '__main__':
    unittest.main()