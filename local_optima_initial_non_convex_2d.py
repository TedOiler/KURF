from simple_GP_temperature.helper_sklearn import get_random_X

class LocalOptimaInit2DNonConvex:
    """
    The class for the initialisation method with local optima for non-convex function
    """

    def generate_initial_samples(self, low=[-100,6.28], high=[100, 6.28], n=1):
        X = get_random_X(low=low, high=high, samples=n).flatten()
        return X