import unittest             # This is the test framework
import the_minimum          # Module under test

class TestMinimumFunctions(unittest.TestCase):   # Test case or Test suite

    def test_collatz(self):             # test method or fixture
        self.assertEqual(the_minimum.collatz(10), 5)
        self.assertEqual(the_minimum.collatz(11), 34)
        self.assertEqual(the_minimum.collatz(0), 0)
        with self.assertRaises(TypeError):
            the_minimum.collatz('hello')
        with self.assertRaises(TypeError):
            the_minimum.collatz(10, 11)
        with self.assertRaises(TypeError):
            the_minimum.collatz()

class TestMinimumClasses(unittest.TestCase):

    def setUp(self):
        self.ee = the_minimum.Employee('Navra Ananda', 'female', 200)

    def test_employee(self):
        navra = self.ee
        self.assertEqual(navra.name, 'Navra Ananda')
        self.assertEqual(navra.gender, 'female')
        self.assertEqual(navra.salary, 200)
        navra.give_raise(10)
        self.assertEqual(navra.salary, 220)        
                
    def test_employee_neg_raise(self):
        navra = self.ee
        self.assertEqual(navra.salary, 200)
        navra.give_raise(-10)
        self.assertEqual(navra.salary, 180)

    def tearDown(self):
        self.ee = None
        

if __name__ == '__main__':

    unittest.main()         # Test runner







