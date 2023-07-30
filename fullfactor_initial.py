import random as rd
class FullFactorInitial2D:
    def __init__(self, fullfactorinput_list):
        self.fullfactorinput_list = fullfactorinput_list


    def generate_initial_samples(self): 
        return_sample = []
        if len(self.fullfactorinput_list) != 0:
            return_sample = self.fullfactorinput_list.pop(0)
        return return_sample