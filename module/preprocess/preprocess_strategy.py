from abc import ABCMeta, abstractmethod
import pandas as pd

class PreprocessStrategy(metaclass=ABCMeta):

    @abstractmethod
    def preprocess(self, data: pd.DataFrame) -> pd.DataFrame:
        pass
