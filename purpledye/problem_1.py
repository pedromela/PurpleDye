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
        
    def test_is_atack_possible1(self):
        result = is_attack_possible((2, 2), (4, 0))
        self.assertEqual(result, True)

    def test_is_atack_possible2(self):
        result = is_attack_possible((2, 2), (4, 3))
        self.assertEqual(result, False)
        
    def count_attacks1(self):
        result = count_attacks([(0, 0), (1, 2), (2, 2), (4, 0)], (0, 0))
        self.assertEqual(result, 1)

    def count_attacks2(self):
        result = count_attacks([(0, 0), (1, 2), (2, 2), (4, 0)], (2, 2))
        self.assertEqual(result, 2)
    
    def is_bishop_on_board1(self):
        result = is_bishop_on_board((2, 2), 5)
        self.assertEqual(result, True)

    def is_bishop_on_board2(self):
        result = is_bishop_on_board((2, -2), 5)
        self.assertEqual(result, False)
    
 
if __name__ == '__main__':
    if(len(sys.argv) == 2 and sys.argv[1] == 'run_tests'):
        unittest.main(argv=[sys.argv[0]])






