from simple_GP_temperature.helper_sklearn import get_random_X_3dp

class LocalOptimaInit2DNonConvex:
    """
    The class for the initialisation method with local optima for non-convex function
    """
    def __init__(self,
                 low=None,
                 high=None,
                 nlargest=1):
        self.low = low
        self.high = high
        self.nlargest = nlargest
    def generate_initial_samples(self, n=1):
        if self.low is not None and self.high is not None:
            X = get_random_X_3dp(low=self.low, high=self.high, samples=n).flatten()
        else:
            low_value = 6.27*self.nlargest
            high_value = 6.29*self.nlargest
            X = get_random_X_3dp(low=[low_value, low_value], high=[high_value, high_value], samples=n).flatten()
        return X