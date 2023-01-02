import unittest
from csproject import *

class TestCsProject(unittest.TestCase):

    def test_createProrfessor_withWrongPassword(self):
        actual = checkUserNameAndPassword("aaa","222222221","222222222")
        expect = False
        
        self.assertEqual(actual, expect, "Create Professor with different password should not pass the BR")

    def test_createProrfessor_withSmallDigitPassword(self):
        actual = checkUserNameAndPassword("aaa","222","222")
        expect = False
        
        self.assertEqual(actual, expect, "Create Professor with small digit password should not pass the BR") 

if __name__ == '__main__':
    unittest.main()