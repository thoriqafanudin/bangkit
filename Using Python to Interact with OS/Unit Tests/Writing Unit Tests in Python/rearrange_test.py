from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Afanudin, Thoriq"
        expected = "Thoriq Afanudin"
        self.assertEqual(rearrange_name(testcase), expected)
        
    def test_empty_string(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)
        
    def test_double_name(self):
        testcase = "Afan, Thoriq U."
        expected = "Thoriq U. Afan"
        self.assertEqual(rearrange_name(testcase), expected)
        
    def test_one_name(self):
        testcase = "Afan"
        expected = "Afan"
        self.assertEqual(rearrange_name(testcase), expected)
        
    def test_number(self):
        testcase = 5
        expected = "5"
        self.assertEqual(rearrange_name(testcase), expected)
        
unittest.main()