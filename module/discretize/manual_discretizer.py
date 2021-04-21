"""Summary
Custom concrete strategy for discretization with auto-denoising
"""
import numpy as np
from .discretization_strategy import DiscretizationStrategy

# class specific constants
min_key = 'min'
interval_key = 'interval'

class ManualDiscretizer(DiscretizationStrategy):

    def __init__(self, features: list, min_values: list, intervals: list) -> None:
        self._feature_map = dict()

        # initializing details for features
        for index, f in enumerate(features):
            self._feature_map[f] = {min_key: min_values[index],
                                    interval_key: intervals[index]}

    def discretize(self, data: np.ndarray, col_name: str) -> np.ndarray:
        """Summary
        Calculates percentiles and gets n_bins between two percentiles
        """
        min_value = self._feature_map[col_name][min_key]
        interval = self._feature_map[col_name][interval_key]

        # Denoising assuming normal distribution
        def disc_fun(x): return (x - min_value) // interval

        return np.array(list(map(disc_fun, data)))
