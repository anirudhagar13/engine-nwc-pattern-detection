from abc import ABCMeta, abstractmethod
import numpy as np
import pandas as pd
from bisect import bisect_left

class NWStrategy(metaclass=ABCMeta):

    @abstractmethod
    def binarize(self, data: pd.DataFrame, target_col: str, invalid_indexes: list) -> np.ndarray:
        pass

    def is_valid_seq(self, start_idx: int, invalid_indexes: list) -> bool:
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

        if len(invalid_indexes) > 0:
            for i in range(start_idx, start_idx + self._window_length - 1):
                if BinarySearch(invalid_indexes, i) != -1:
                    return False

        return True
