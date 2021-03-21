import unittest
import numpy as np
import pandas as pd
from module.nc_window import MeanThresholdBinarizer


class TestMeanThresholdBinarizer(unittest.TestCase):

    threshold = 1700
    window_length = 3
    data = np.array([2030, 2388, 1954, 1775, 1780, 1817, 2026, 832,
                     2009, 1052, 1225, 1365, 2489, 1925, 807, 2241,
                     1365, 1547, 2216, 818])
    target_data = pd.DataFrame({'Target': data})

    def test_binarize(self):
        exp_binary = [1, 1, 1, 1, 1, 0, 0, 0,
                      0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0]

        bin_obj = MeanThresholdBinarizer(
            self.threshold, self.window_length)

        self.assertListEqual(bin_obj.binarize(
            self.target_data, 'Target', list()).tolist(), exp_binary)

    def test_binarize_with_idx(self):
        invalid_idx = [4, 12, 15]
        exp_binary = [1, 1, 0, 0, 1, 0, 0, 0,
                      0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0]

        bin_obj = MeanThresholdBinarizer(
            self.threshold, self.window_length)

        self.assertListEqual(bin_obj.binarize(
            self.target_data, 'Target', invalid_idx).tolist(), exp_binary)


if __name__ == '__main__':
    unittest.main()
