"""Summary
Custom concrete strategy for discretization with auto-denoising
"""
import numpy as np
from sklearn.preprocessing import KBinsDiscretizer
from .discretization_strategy import DiscretizationStrategy

# class specific constants
highest_percentile = 100

class DenoiseDiscretizer(DiscretizationStrategy):

    """Summary
    To discretize continuous data into ordinals with a custom strategy to denoise
    """

    def __init__(self, n_bins: int):
        self._n_bins = n_bins

    def discretize(self, data: np.ndarray) -> np.ndarray:
        """Summary
        Calculates percentiles and gets n_bins between two percentiles
        """
        mean, std = data.mean(), data.std()

        # Denoising assuming normal distribution
        higher_margin = mean + std
        lower_margin = mean - std

        gap = higher_margin - lower_margin
        bin_width = int(gap / self._n_bins) + 1

        max_num, min_num = data.max(), data.min()
        bins = [i for i in range(int(min_num), int(max_num), bin_width)]

        return np.digitize(data, bins)
