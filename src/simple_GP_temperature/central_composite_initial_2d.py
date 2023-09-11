from pyDOE2 import ccdesign


class CentralCompInit2D:
    """
    The class for the initialisation method with generalised central composite around local optima for 2D non-convex function

    """
    def __init__(self,
                 low=None, #lowerbound
                 high=None, #upperbound
                 nlargest=1,
                 center=None, # A 2-tuple of center point(one for factorial block one for axial block)
                ):
        self.low = low #lowerbound
        self.high = high #upperbound
        self.nlargest = nlargest
        self.center = center
        self.central_comp_matrix = list(self.__generate_central_composite_samples())

    def generate_initial_samples(self):
        """
        Pop one of the initial sample from the pre-generated full-factorial list
        :return: list[x1, x2] A unidimensional list of 2D initial input
        """
        assert len(self.central_comp_matrix)>0, 'The Generated central composite samples must be larger or equal to the initial sample size'
        returned_sample = self.central_comp_matrix.pop(0)
        return returned_sample


    def __generate_central_composite_samples(self):
        """
        A function that generates the central composite initial samples
        :return: Numpy 2D Array  A 2D Array of experimental matrix
        """
        design_matrix = ccdesign(2, center=self.center, face = 'cci') # check this for the details of face https://pythonhosted.org/pyDOE/rsm.html#response-surface
        returned_matrix = design_matrix*((self.high-self.low)/2) + ((self.high+self.low)/2)
        return returned_matrix