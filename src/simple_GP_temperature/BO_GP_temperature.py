import math
import numpy as np

from sklearn.gaussian_process import GaussianProcessRegressor
from scipy.stats import norm
from simple_GP_temperature.helper_sklearn import opt_acq
import pandas as pd
import pdb

class BOTemperatureGP:
    """
    The gaussian process model for optimising the temperature of the reaction
    """
    def __init__(self,
                 evaluation_component,
                 upper_bound,
                 lower_bound,
                 initial_method,
                 initial_sample_size = 8,
                 total_iter = 50, #number of total iterations
                 #fnum = 8, #number of features (Top K)
                ):
        self.evaluation_component = evaluation_component
        self.initial_method = initial_method
        self.init_sample_size = initial_sample_size
        #self.fnum = fnum
        self.total_iter = total_iter
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

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
        training_samples = []
        evaluation_scores = []

        while len(training_samples) < self.init_sample_size:
            init_sample = self.initial_method.generate_initial_samples()
            if not np.isin(np.array(init_sample), np.array(training_samples)).all():
                training_samples.append(init_sample)
                score = self.evaluation_component.get_evaluation_score(init_sample)
                evaluation_scores.append(score)

        model = self.__train_gp_model(training_samples, evaluation_scores)

        for i in range(self.total_iter):
            next_sample_to_be_evaluated = opt_acq(X=np.array(training_samples), y=np.array(evaluation_scores), model=model, low=self.lower_bound, high=self.upper_bound)
            score = self.evaluation_component.get_evaluation_score(next_sample_to_be_evaluated)
            training_samples.append(next_sample_to_be_evaluated)
            evaluation_scores.append(score)
            model = self.__train_gp_model(training_samples, evaluation_scores)
            # print(f'next sample to be evaluated: {next_sample_to_be_evaluated}, score: {score}')

        temp_score_mapping = {tuple(training_samples[index]): evaluation_scores[index] for index in
                               range(len(training_samples))}

        return temp_score_mapping
