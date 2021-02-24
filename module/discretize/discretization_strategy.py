from abc import ABCMeta, abstractmethod
import numpy as np

class DiscretizationStrategy(metaclass=ABCMeta):

    @abstractmethod
    def discretize(self, data: np.ndarray) -> np.ndarray:
        pass
