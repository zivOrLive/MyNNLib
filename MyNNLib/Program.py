# from BL.Activation_Functions.RELU import RELU
# from BL.Activation_Functions.Softmax import Softmax
# from BL.Cost_Functions.Log_likelihood import Log_likelihood
# from BL.DataLoader import DataLoader
# from BL.HyperParameterContainer import HyperParameterContainer
# from BL.Layers.Convolutional import Convolutional
# from BL.Layers.FullyConnected import FullyConnected
# from BL.Layers.MaxPooling import MaxPooling
# from BL.Network import Network
# from BL.Gradient_Decent.MomentumBased import MomentumBased
# from BL.Regularization.Dropout import Dropout
# from DAL.Mongo.MongoDB import MongoDB
#
# # TODO: Understand how fftconvolve works
# # TODO: Design the system better so it will keep all the SOLID principles
# # TODO: How to reshape the output from convolutional to the correct shape in Max pooling
#
# training_set, validation_set, test_set = DataLoader.load()
# activationFunc = RELU()
# dropout = Dropout((5, 6, 7), number_of_runs=10)
#
# HyperParameterContainer.init(
#     gradientDescent = MomentumBased(5)
# )
#
# layers = [
#     Convolutional(
#         sizeOfLocalReceptiveField=(5, 5),
#         numberOfFilters=20,
#         sizeOfInputImage=(28, 28),
#         stride=1,
#         numberOfInputFeatureMaps=1
#     ),
#     MaxPooling(
#         sizeOfInputImage=(24, 24),
#         stride=1,
#         poolSize=(2, 2),
#         number_of_input_feature_maps=20
#     ),
#     Convolutional(
#         sizeOfLocalReceptiveField=(5, 5),
#         numberOfFilters=40,
#         sizeOfInputImage=(12, 12),
#         stride=1,
#         numberOfInputFeatureMaps=20
#     ),
#     MaxPooling(
#         sizeOfInputImage=(12, 12),
#         stride=1,
#         poolSize=(2, 2),
#         number_of_input_feature_maps=40
#     ),
#     FullyConnected(
#         n_in=40 * 4 * 4,
#         n_out=1000
#     ),
#     FullyConnected(
#         n_in=1000,
#         n_out=1000
#     ),
#     FullyConnected(
#         n_in=1000,
#         n_out=10,
#         isSoftmax=True
#     )
# ]
#
# model = Network(
#     costFunction=Log_likelihood(),
#     last_layer_activation_function=Softmax(),
#     layers=layers,
#     training_set=training_set,
#     validation_set=validation_set,
#     test_set=test_set,
#     db=MongoDB(),
#     should_load_from_db=False,
#     should_save_to_db=True,
#     network_id="1",
#     should_regulate=True,
#     regularizationTechs=(dropout)
# )
#
# model.runNetwork()
#
from scipy.signal import fftconvolve
import numpy as numpy

from BL.Layers.MathHelper import _MathHelper

"""
the matrix shape is: 
mini_batch_size X
numberOfFilters X
numberOfInputFeatureMaps X
sizeOfInputImage[0] X 
sizeOfInputImage[1]  

the kernel shape is:
mini_batch_size X 
numberOfFilters X 
sizeOfLocalReceptiveField[0] X  
sizeOfLocalReceptiveField[1]
"""
matrix = numpy.arange(784).reshape((1,1, 1, 28, 28))
kernel = numpy.arange(25).reshape((1, 1, 5, 5))


print(_MathHelper.conv5D(matrix, kernel, 1).shape)
