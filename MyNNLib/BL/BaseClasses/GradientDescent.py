from abc import ABC, abstractmethod

class GradientDescent(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def changeWeights(self, w, gradient):
        pass

    @abstractmethod
    def changeBiases(self, b, gradient):
        pass