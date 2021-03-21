from abc import ABCMeta, abstractmethod
import numpy as np
import pandas as pd

class NWStrategy(metaclass=ABCMeta):

    @abstractmethod
    def binarize(self, data: pd.DataFrame, target_col: str, invalid_indexes: list) -> np.ndarray:
        pass
