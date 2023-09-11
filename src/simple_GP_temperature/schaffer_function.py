import numpy as np

class SchafferFunction:
    """
    Class for objective function Schaffer
    """
    def get_evaluation_score(self, X, noise_scale=0.01):
        """
        Get the value of the schaffer function with input X
        :param X: array([float, float]) A numpy array of the input coordinate
        :param noise_scale: float the scale of noise we would like to have
        :return:
        """
        if len(X) != 2:
            raise ValueError("The length of input value must be equal to 2")

        noise = np.random.normal(loc=0, scale=noise_scale)
        num = np.sin(X[0] ** 2 - X[1] ** 2) ** 2 - 0.5
        denom = 1 + 0.1 * (X[0] ** 2 + X[1] ** 2)
        func = 20 - 20*num/denom

        return func + noise