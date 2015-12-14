import unittest
from mock import *
from Basic import *

class TestBasic(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestBasic, self).__init__(*args, **kwargs)
        self.o = Basic()






    def testFact(self):
        ''' A basic unit test '''
        self.assertEqual(self.o.fact(1), 1)
        self.assertEqual(self.o.fact(4), 24)
        self.assertEqual(self.o.fact(1), 1)






    def testGenFact(self):
        ''' Basic unit test using the generation class '''
        gen = Gen()
        self.assertEqual(self.o.genfact(gen), 1)
        self.assertEqual(self.o.genfact(gen), 2)
        self.assertEqual(self.o.genfact(gen), 6)
        self.assertEqual(self.o.genfact(gen), 24)







    def testGenFact2(self):
        ''' Now let's patch the generation class to return a constant value '''
        with patch.object(Gen, 'get', return_value=3) as mocked:
            gen = Gen()
            self.assertEqual(self.o.genfact(gen), 6)
            self.assertEqual(self.o.genfact(gen), 6)
            self.assertEqual(self.o.genfact(gen), 6)

        self.assertEqual(mocked.call_count, 3)






    @patch.object(Gen, 'get', return_value=3)
    def testGenFact2(self, mocked):
        ''' Patching the class, take 2:  Do it with a decorator'''
        gen = Gen()
        self.assertEqual(self.o.genfact(gen), 6)
        self.assertEqual(self.o.genfact(gen), 6)
        self.assertEqual(self.o.genfact(gen), 6)

        self.assertEqual(mocked.call_count, 3)






    def testGenFact2(self):
        '''Demonstrate why we might use a 'with' statement -- different mocks'''
        with patch.object(Gen, 'get', return_value=3) as mocked:
            gen = Gen()
            self.assertEqual(self.o.genfact(gen), 6)
            self.assertEqual(self.o.genfact(gen), 6)
            self.assertEqual(mocked.call_count, 2)

        with patch.object(Gen, 'get', return_value=4) as mocked:
            gen = Gen()
            self.assertEqual(self.o.genfact(gen), 24)






    def testFact(self):
        '''Now an interesting case -- we're going to use mock to count how many times and how fact is called'''
        with patch.object(self.o, 'fact', wraps=self.o.fact) as mocked:
            with patch.object(self.o, 'genfact', wraps=self.o.genfact) as mgen:
                self.assertEqual(self.o.fact(4), 24)
                self.assertEqual(mocked.call_count, 4)

                mocked.assert_any_call(4)
                mgen.assert_not_called()





if __name__ == '__main__':
    unittest.main()
