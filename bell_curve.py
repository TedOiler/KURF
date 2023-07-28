import numpy as np

class Bellcurve:
    """
    Class for objective function Bell Curve
    """
    def get_evaluation_score(self, X, noise_scale=0.01):
        """
        Get the value of the function with input X
        :param X: array([float, float]) A numpy array of the input coordinate
        :param noise_scale: float the scale of noise we would like to have
        :return:
        """
        noise = np.random.normal(loc=0, scale=noise_scale)
        bellcurve = (4*np.exp(-X[0]**2) + 6*np.exp(-4*X[1]**2))

        return bellcurve+noise