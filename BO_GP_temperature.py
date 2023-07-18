import math
import numpy as np
from sklearn.gaussian_process.kernels import ConstantKernel
from sklearn.gaussian_process.kernels import WhiteKernel
from sklearn.gaussian_process.kernels import RBF
from sklearn.gaussian_process.kernels import Matern
from sklearn.gaussian_process import GaussianProcessRegressor
import pdb
from scipy.stats import norm
from helper_sklearn import *
import pandas as pd

class BOTemperatureGP:
    """
    The gaussian process model for optimising the temperature of the reaction
    """
    def __init__(self,
                 evaluation_component,
                 initial_method,
                 initial_sample_size = 20,
                 total_iter = 250, #number of total iterations
                 #fnum = 8, #number of features (Top K)
                ):
        self.evaluation_component = evaluation_component
        self.initial_method = initial_method
        self.init_sample_size = initial_sample_size
        #self.fnum = fnum
        self.total_iter = total_iter

    def __train_gp_model(self, training_samples, evaluation_scores):
        """
        Train the Gaussian Process surrogate model
        :param training_samples: list[list[float]] A list of temperatures
        :param evaluation_scores: list[float] Alist of evaluation scores (yield - e-factor) for the train
        :return: The gaussian process model
        """
        model = GaussianProcessRegressor()
        model.fit(np.array(training_samples), np.array(evaluation_scores))

        return model

    def optimise(self):
        """
        Optimise the temperature to increase the yield and decrease the e-factor
        :return: {(temperatures, evaluation_scores)}
        """
        temperatures = []
        evaluation_scores = []

        while len(temperatures) < self.init_sample_size:
            temperature = self.initial_method.generate_initial_samples()
            if temperature not in temperatures:
                temperatures.append(temperature)
                score = self.evaluation_component.get_evaluation_score(temperature=temperature[0])
                evaluation_scores.append(score)

        model = self.__train_gp_model(temperatures, evaluation_scores)

        for i in range(self.total_iter):
            best_expected_temperature = opt_acq(X=np.array(temperatures), y=np.array(evaluation_scores), model=model)
            score = self.evaluation_component.get_evaluation_score(temperature=best_expected_temperature)
            temperatures.append([float(best_expected_temperature)])
            evaluation_scores.append(score)
            model = self.__train_gp_model(temperatures, evaluation_scores)
            #print(f'current temperature to be evaluate: {float(best_expected_temperature)}, score: {score}')

        temp_score_mapping = {tuple(temperatures[index]): evaluation_scores[index] for index in
                               range(len(temperatures))}
        
        print(temp_score_mapping)
        return temp_score_mapping
