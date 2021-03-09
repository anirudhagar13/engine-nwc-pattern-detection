"""Summary
Default concrete strategy for binarizing target
"""
import numpy as np
import pandas as pd
from bisect import bisect_left
from .noncompliant_window_strategy import NWStrategy

class MeanThresholdBinarizer(NWStrategy):

    def __init__(self, threshold: float, window_length: int, invalid_indexes: list):
        """
        Args:
            threshold (float): Average threshold for non-compliant behavior
            window_length (int): Window length over which patterns to be analysed
            invalid_indexes (list): Indexes across which sequences are not valid
        """
        self._threshold = threshold
        self._window_length = window_length
        self._invalid_indexes = invalid_indexes

    def binarize(self, data: pd.DataFrame, target_col: str) -> np.ndarray:
        """Summary
        Takes continuous data and binarize using threshold as 0 or 1
        """
        # selecting target and index data
        tgt_data = data[target_col].to_numpy()
        wlen = self._window_length

        # Using for loop instead of list comprehension, due to interpretability
        binary_data = [0] * len(data)
        for i in range(len(data) - wlen):

            # Verifies if sequence is not across any of violated indexes or does
            # not end on a violated index (can start from it)
            if self.is_valid_seq(i + 1):

                # Evaluates if mean of values within
                if (tgt_data[i:i + wlen].sum() / wlen) > self._threshold:
                    binary_data[i] = 1

        return np.array(binary_data)

    def is_valid_seq(self, start_idx: int) -> bool:
        """Summary
        Determines if current sequence is across any of violated indexes
        Args:
            start_idx (int): starting index of a sequence
        """
        # Most elegant and fast solution

        def BinarySearch(a: list, x) -> int:
            i = bisect_left(a, x)
            if i != len(a) and a[i] == x:
                return i
            else:
                return -1

        if len(self._invalid_indexes) > 0:
            for i in range(start_idx, start_idx + self._window_length - 1):
                if BinarySearch(self._invalid_indexes, i) != -1:
                    return False

        return True
