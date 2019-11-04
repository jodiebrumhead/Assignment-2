"""Test module to unit test the loaddata.loadData function"""

# load useful modules
import unittest
import numpy
# load module to test
from Load import loaddata


class Testloaddata(unittest.TestCase):

    def setUp(self):
        self.x, self.y = loaddata.loadData('../plenty.data')

    def test_loadData(self):
        self.assertIsNotNone(self.x)  # test x and y are not empty??
        self.assertIsNotNone(self.y)  # test x and y are not empty??
        self.assertEqual(len(self.x), len(self.y))  # test x and y have equal number of rows?
        self.assertEqual(type(self.x), numpy.ndarray)  # test x and y = numpy array
        self.assertEqual(type(self.y), numpy.ndarray)  # test x and y = numpy array
        # would also like to test that values stored in x and y are floats

# would be best to test with other data too


# allows test code to be run directly
if __name__ == '__main__':
    unittest.main()