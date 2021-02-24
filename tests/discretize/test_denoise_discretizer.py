import unittest
from module.discretize.denoise_discretizer import *

class TestDefaultDiscretizer(unittest.TestCase):

    def test_discretize(self):
        n_bins = 10
        data = np.array([100, 200, 300, 150, 2216, 2012, 2170, 2162, 1817, 2252, 1660,
                         1265, 2305, 844, 1095, 1631, 1570, 956, 2261, 1680, 1642, 1303,
                         2041, 2385, 3200, 3500, 3100, 4000])
        disc_data = [1, 1, 2, 1, 11, 10, 11, 11, 9, 12, 9, 7, 12,
                     4, 6, 8, 8, 5, 12, 9, 8, 7, 11, 12, 16, 18, 16, 21]

        disc_obj = DenoiseDiscretizer(n_bins)

        self.assertListEqual(disc_obj.discretize(data).tolist(), disc_data)


if __name__ == '__main__':
    unittest.main()
