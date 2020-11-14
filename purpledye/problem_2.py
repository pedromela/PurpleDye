import sys
import unittest

def is_pal(pal_cand):
    return pal_cand == pal_cand[::-1]
    
def problem2(input_string):
    len_string = len(input_string)
    pals = []
    
    pal_ini_idx = 0
    while pal_ini_idx < len_string:
        pal_end_idx = len_string-1
        
        while pal_end_idx>=pal_ini_idx:
            pal_cand = input_string[pal_ini_idx:pal_end_idx+1]
            if is_pal(pal_cand):
                pals.append(pal_cand)
                pal_ini_idx=pal_end_idx
            pal_end_idx-=1
        pal_ini_idx+=1
    
    return pals        


class Problem2Tests(unittest.TestCase):
    def testOk1(self):
        result = problem2("racecarannakayak")
        self.assertEqual(result, ["racecar", "anna", "kayak"])
        
    def testOk2(self):
        result = problem2("abc")
        self.assertEqual(result, ["a", "b", "c"])
    
    def testEmptyData(self):
        result = problem2("")
        self.assertEqual(result, [])
        
    def testSameRepeatedLetter(self):
        result = problem2("aaa")
        self.assertEqual(result, ["aaa"])

if(len(sys.argv) == 2 and sys.argv[1] == 'run_tests' and __name__ == '__main__'):
    unittest.main(argv=[sys.argv[0]])

