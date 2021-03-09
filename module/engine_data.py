import pandas as pd
from discretize import *
from preprocess import *
from nc_window import *

class EngineData:

    def __init__(self, data, pd.DataFrame):
        self._data = data
        self._preprocess_strategy = PreprocessStrategy()
        self._discretize_strategy = DiscretizationStrategy()
        self._binarize_strategy = NWStrategy()

    def preprocess(self):
        return self._preprocess_strategy.preprocess(self._data)

    def __str__(self):
        return self._data.describe()
