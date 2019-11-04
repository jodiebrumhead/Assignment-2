"""Test module to unit test the translator.transtable function"""

# load useful modules
import unittest
# load module to test
from Load import translator


class TestTranslator(unittest.TestCase):
    def test_transtable(self):
        self.assertEqual(translator.transtable(), {40: None, 41: None, 10: None, 91: None, 93: None})
        # check the dictionary continues to be created as expected
        # especially useful for testing if code works correctly post updates
        self.assertEqual('ljbl()'.translate(translator.transtable()), 'ljbl')
        self.assertEqual('ljbl[]'.translate(translator.transtable()), 'ljbl')
        # check string.translate using transtable continues to work as expected in removing unwanted characters


# allows test code to be run directly
if __name__ == '__main__':
    unittest.main()


