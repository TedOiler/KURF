import numpy as np

class AckleyFunction:
    """
    Class for objective function Ackley
    """
    def get_evaluation_score(self, X, noise_scale=0.01):
        """
        Get the value of the Ackley function with input X
        :param X: array([float, float]) A numpy array of the input coordinate
        :param noise_scale: float the scale of noise we would like to have
        :return:
        """
        if len(X) != 2:
            raise ValueError("The length of input value must be equal to 2")

        noise = np.random.normal(loc=0, scale=noise_scale)
        a = 20
        b = 0.2
        c = 2 * np.pi
        sum1 = X[0] ** 2 + X[1] ** 2
        sum2 = np.cos(c * X[0]) + np.cos(c * X[1])
        func = a * np.exp(-b * np.sqrt(sum1 / 2)) + np.exp(sum2 / 2) + a + np.exp(1)

        return func + noise