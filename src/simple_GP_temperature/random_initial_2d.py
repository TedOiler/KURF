from simple_GP_temperature.helper_sklearn import get_random_X

class RandomInit2D:
    def generate_initial_samples(self, low=[-10,-10], high=[10, 10], n=1):
        X = get_random_X(low=low, high=high, samples=n).flatten()
        return X