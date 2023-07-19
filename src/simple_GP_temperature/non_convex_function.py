import numpy as np

class NonConvexFunction:
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

        func = -(X[0] ** 2 + X[1] ** 2) + 2 * np.cos(X[0]) * np.cos(X[1])

        return func+noise