import random as rd

class RandomInit:
    """
        The class for generating random initial samples
    """
    def __init__(self,
                 lower_bound,
                 upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def generate_initial_samples(self):
        """
        Generate initial samples with lower-bound and upperbound
        :return: List[float] A list of random initial samples
        """
        initial_samples = []
        random_sample = float(round(rd.uniform(self.lower_bound, self.upper_bound), 2))
        initial_samples.append(random_sample)

        return initial_samples

