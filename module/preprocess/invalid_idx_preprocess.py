"""Summary
Pre-process data and returns data indexes across which sequences should not be formed
Abstracting concepts like Iteration and Trips in specific engine data
"""
import pandas as pd
from .preprocess_strategy import PreprocessStrategy

class InvalidIndexPreprocessor(PreprocessStrategy):

    def __init__(self, split_cols: list, index_cols: list):
        """
        Args:
            split_cols (list): List of columns that should be same in a sequence
            index_cols (list): List of columns that should consecutive in a sequence
        """
        self._split_cols = split_cols
        self._index_cols = index_cols

    def preprocess(self, data: pd.DataFrame) -> list:
        """Summary
        Returns indexes across which sequences are not valid
        """
        invalid_idx = list()

        for col in self._index_cols:
            invalid_idx.extend(self.invalid_index_idxes(data[col]))

        for col in self._split_cols:
            invalid_idx.extend(self.invalid_split_idxes(data[col]))

        return list(sorted(set(invalid_idx)))

    def invalid_split_idxes(self, data: pd.Series) -> list:
        """Summary
        Returns indexes where data value changes
        """
        return [i + 1 for i in range(len(data) - 1) if data[i + 1] != data[i]]

    def invalid_index_idxes(self, data: pd.Series) -> list:
        """Summary
        Returns indexes where data value is not continuous
        """
        return [i + 1 for i in range(len(data) - 1) if data[i + 1] - data[i] != 1]
