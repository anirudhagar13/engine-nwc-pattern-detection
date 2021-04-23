import unittest
import numpy as np
import pandas as pd
from module.preprocess import InvalidIndexPreprocessor

class TestInvalidIndexPreprocessor(unittest.TestCase):

    def test_preprocess(self):
        iter_col = np.array([2, 3, 4, 5, 6, 7, 9, 10, 11,
                             12, 13, 14, 17, 18, 19, 20, 21, 23, 24, 25])

        pass_col = np.array([1, 1, 1, 2, 2, 2, 2, 2, 2, 2,
                             2, 2, 2, 2, 2, 3, 3, 3, 3, 3])

        year_col = np.array([2019, 2019, 2019, 2019, 2019, 2020, 2020, 2020,
                             2020, 2020, 2021, 2021, 2021, 2021, 2021, 2021,
                             2021, 2021, 2021, 2022])

        data = np.array([2030, 2388, 1954, 1775, 1780, 1817, 2026, 832,
                         2009, 1052, 1225, 1365, 2489, 1925, 807, 2241,
                         1365, 1547, 2216, 818])

        target_data = pd.DataFrame(
            {'NC': data, 'Pass': pass_col, 'Iter': iter_col, 'Year': year_col})
        exp_invalid_idx = [3, 5, 6, 10, 12, 15, 17, 19]

        preprocess_obj = InvalidIndexPreprocessor(['Pass', 'Year'], ['Iter'])

        self.assertListEqual(preprocess_obj.preprocess(
            target_data), exp_invalid_idx)


if __name__ == '__main__':
    unittest.main()
