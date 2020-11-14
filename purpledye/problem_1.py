import sys
import unittest

def is_attack_possible(bishop_1, bishop_2):
    return abs(bishop_1[0] - bishop_2[0]) == abs(bishop_1[1] - bishop_2[1])

def count_attacks(ref_bishop, bishops):
    return sum([is_attack_possible(ref_bishop, bishop) for bishop in bishops])

def is_bishop_on_board(bishop,M):
    x,y = bishop
    return not(x<0 or y<0 or x>=M or y>=M)

def problem1(bishops, M):
    bishops = [bishop for bishop in bishops if is_bishop_on_board(bishop,M)]
    return sum([count_attacks(bishop, bishops[i+1:]) for i, bishop in enumerate(bishops)])

    
class Problem1Tests(unittest.TestCase):
    def testOk1(self):
        result = problem1([(0, 0), (1, 2), (2, 2), (4, 0)],5)
        self.assertEqual(result, 2)
        
    def testOk2(self):
        result = problem1([(0, 0), (1, 2), (2, 2), (4, 0), (6, 5), (7, 7), (8, 6), (9, 3), (0, 4)],10)
        self.assertEqual(result, 7)
        
    def testNegativeData(self):
        result = problem1([(0, 0), (-1, -2), (-2, -2), (-4, 0)],5)
        self.assertEqual(result, 0)
    
    def testEmptyData(self):
        result = problem1([],5)
        self.assertEqual(result, 0)
 
if(len(sys.argv) == 2 and sys.argv[1] == 'run_tests' and __name__ == '__main__'):
    unittest.main(argv=[sys.argv[0]])







