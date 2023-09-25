import dexpy.optimal as optimal
import numpy as np

class DOptimalInit2D:
    """
    The class for the initialisation method with generalised D-optimal Design around local optima for 2D non-convex function

    """
    def __init__(self,
                 low=None, #lowerbound
                 high=None, #upperbound
                 nlargest=1,
                 sample_size=5,
                ):
        self.low = low #lowerbound
        self.high = high #upperbound
        self.nlargest = nlargest
        self.sample_size = sample_size
        self.d_optimal_matrix = list(self.__generate_d_optimal_samples())

    def generate_initial_samples(self):
        """
        Pop one of the initial sample from the pre-generated D-optimal design list
        :return: list[x1, x2] A unidimensional list of 2D initial input
        """
        if len(self.d_optimal_matrix) <= 0:
            self.d_optimal_matrix = list(self.__generate_d_optimal_samples())
        returned_sample = self.d_optimal_matrix.pop(0)
        return returned_sample


    def __generate_d_optimal_samples(self):
        """
        A function that generates the central composite initial samples
        :return: Numpy 2D Array  A 2D Array of experimental matrix
        """
        design_matrix = np.array((optimal.build_optimal(2, run_count = self.sample_size)).values.tolist())
        returned_matrix = design_matrix*((self.high-self.low)/2) + ((self.high+self.low)/2)
        return returned_matrix