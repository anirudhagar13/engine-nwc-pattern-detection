"""Summary
Default concrete strategy for binarizing target
"""
import numpy as np
import pandas as pd
from .noncompliant_window_strategy import NWStrategy

class MeanThresholdBinarizer(NWStrategy):

    def __init__(self, threshold: float, window_length: int):
        """
        Args:
            threshold (float): Average threshold for non-compliant behavior
            window_length (int): Window length over which patterns to be analysed
        """
        self._threshold = threshold
        self._window_length = window_length

    def binarize(self, data: pd.DataFrame, target_col: str,
                 invalid_indexes: list) -> np.ndarray:
        """Summary
        Takes continuous data and binarize using threshold as 0 or 1
        Args:
            target_col: column name to be used to create anomalous windows
            invalid_indexes (list): Indexes across which sequences are not valid
        """
        # selecting target and index data
        tgt_data = data[target_col].to_numpy()
        wlen = self._window_length

        # Using for loop instead of list comprehension, due to interpretability
        binary_data = [0] * len(data)
        for i in range(len(data) - wlen):

            # Verifies if sequence is not across any of violated indexes or does
            # not end on a violated index (can start from it)
            if super().is_valid_seq(i + 1, invalid_indexes):

                # Evaluates if mean of values within
                if (tgt_data[i:i + wlen].sum() / wlen) > self._threshold:
                    binary_data[i] = 1

        return np.array(binary_data)
