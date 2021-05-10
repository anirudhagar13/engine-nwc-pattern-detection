import pandas as pd

from .constants import target_col_name
from .discretize import DiscretizationStrategy
from .preprocess import PreprocessStrategy
from .nc_window import NWStrategy

class EngineData:

    def __init__(self, data: pd.DataFrame,
                 preprocess_strategy: PreprocessStrategy,
                 discretize_strategy: DiscretizationStrategy,
                 binarize_strategy: NWStrategy):
        self._data = data
        self._preprocess_strategy = preprocess_strategy
        self._discretize_strategy = discretize_strategy
        self._binarize_strategy = binarize_strategy

    def preprocess(self):
        return self._preprocess_strategy.preprocess(self._data)

    def binarize(self, invalid_indexes: list, nc_window_col_name: str):
        self._data[target_col_name] = self._binarize_strategy.binarize(
            self._data, nc_window_col_name, invalid_indexes)

    def discretize(self, feature_col_names):
        # discretizes each column one by one
        for c in feature_col_names:
            arr_data = self._data[c].to_numpy()
            self._data[c] = self._discretize_strategy.discretize(arr_data, c)

    def prepare_data(self, nc_window_col_name: str, feature_col_names: list):
        '''
        Prepare engine data by;
                - preprocessing and finding out invalid indexes (across which seq are invalid)
                - discretizing continuous data of specific columns
                - binarizing anomalous window column
        '''
        invalid_indexes = self.preprocess()
        print('Count of Invalid Seq Indexes: ', len(invalid_indexes))
        print('\n', '-' * 20, ' | ',
              'Completed Engine Data Preprocessing', ' | ', '-' * 20, '\n')

        self.binarize(invalid_indexes, nc_window_col_name)
        num_of_nc_windows = (
            self._data[target_col_name].to_numpy() == 1).sum()
        print('\n', '-' * 20, ' | ', 'Completed Finding Anomalous Windows: ',
              num_of_nc_windows, ' | ', '-' * 20, '\n')

        # raise issue if no windows found
        if num_of_nc_windows == 0:
            raise Exception('No Anomalous Window found. Adjust threshold.')

        print(self._data[feature_col_names].describe())
        self.discretize(feature_col_names)
        print('\n', '-' * 20, ' | ',
              'Completed Discretizing Feature Columns', ' | ', '-' * 20, '\n')

        return invalid_indexes, self._data

    def __str__(self):
        return self._data.describe()
