from abc import ABC, abstractmethod

from BL.BaseClasses.CostRegularization import CostRegularization


class GradientDescent(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def changeWeights(self, w, gradient, learningRate, mini_batch_size):
        pass

    @abstractmethod
    def changeBiases(self, b, gradient, learningRate, mini_batch_size):
        pass