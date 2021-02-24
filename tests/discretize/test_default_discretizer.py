import unittest
from module.discretize.default_discretizer import *

class TestDefaultDiscretizer(unittest.TestCase):

    def test_discretize(self):
        n_bins = 10
        data = np.array([90, 18, 36, 30, 95, 83, 2, 76, 30, 97, 65, 33])
        disc_data = [9, 2, 4, 3, 10, 9, 1, 8, 3, 10, 7, 4]

        disc_obj = DefaultDiscretizer(n_bins)

        self.assertListEqual(disc_obj.discretize(data).tolist(), disc_data)


if __name__ == '__main__':
    unittest.main()
