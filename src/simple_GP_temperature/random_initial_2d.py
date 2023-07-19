from simple_GP_temperature.helper_sklearn import get_random_X

class RandomInit2D:
    def generate_initial_samples(self, low=[-100,-100], high=[100, 100], n=1):
        X = get_random_X(low=low, high=high, samples=n).flatten()
        return X