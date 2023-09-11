from pyDOE2 import fullfact
import random as rd

class FullFacInit2D:
    """
    The class for the initialisation method with generalised Full-Factorial around local optima for 2D non-convex function

    """
    def __init__(self,
                 low=None, #lowerbound
                 high=None, #upperbound
                 nlargest=1,
                 levels=None, # The levels for each input factor e.g. [3,3] means 3 levels for the first factor and 3 levels for the second factor
                 ):
        self.low = low #lowerbound
        self.high = high #upperbound
        self.nlargest = nlargest
        self.levels = levels
        self.full_fact_matrix = list(self.__generate_full_factorial_samples())

    def generate_initial_samples(self):
        """
        Pop one of the initial sample from the pre-generated full-factorial list
        :return: list[x1, x2] A unidimensional list of 2D initial input
        """
        assert len(self.full_fact_matrix)>0, 'The Generated full factorial samples must be larger or equal to the initial sample size'
        returned_sample = self.full_fact_matrix.pop(0)
        return returned_sample


    def __generate_full_factorial_samples(self):
        """
        A function that generates the Full Factorial initial samples
        :return: Numpy 2D Array  A 2D Array of experimental matrix
        """
        design_matrix = fullfact(self.levels)
        for i in range(max(self.levels)):
            design_matrix[design_matrix == int(i)] = self.low + i*((self.high - self.low)/(max(self.levels)-1))
        returned_matrix = design_matrix
        return returned_matrix
