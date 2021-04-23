"""Summary
Default concrete strategy for discretization
"""
import numpy as np
from .discretization_strategy import DiscretizationStrategy

class DefaultDiscretizer(DiscretizationStrategy):

    def __init__(self, n_bins: int):
        self._n_bins = n_bins

    def discretize(self, data: np.ndarray, col_name: str = '') -> np.ndarray:
        """Summary
        Takes continuous data and discretizes
        """
        max_num, min_num = data.max(), data.min()
        bin_width = int((max_num - min_num) / self._n_bins) + 1
        bins = [i for i in range(int(min_num), int(max_num), bin_width)]

        return np.digitize(data, bins)
