"""Summary
Custom concrete strategy for discretization with auto-denoising
"""
import numpy as np
from .discretization_strategy import DiscretizationStrategy

class DenoiseDiscretizer(DiscretizationStrategy):

    def __init__(self, n_bins: int):
        self._n_bins = n_bins

    def discretize(self, data: np.ndarray, col_name: str = '',
                   n_min: float = 1.8,
                   n_max: float = 3) -> np.ndarray:
        """Summary
        Calculates percentiles and gets n_bins between two percentiles
        """
        mean, std = data.mean(), data.std()

        # Denoising assuming normal distribution
        higher_margin = mean + n_max * std
        lower_margin = mean - n_min * std

        # prevent lower_margin from being zero
        lower_margin = lower_margin if lower_margin > 0 else 0

        gap = higher_margin - lower_margin
        bin_width = int(gap / self._n_bins) + 1

        # Denoising assuming normal distribution
        def disc_fun(x): return int((x - lower_margin) // bin_width)

        # cutting out negative values
        disc_values = np.array(list(map(disc_fun, data)))
        disc_values[disc_values < 0] = 0

        return disc_values
