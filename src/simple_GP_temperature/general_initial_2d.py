import random as rd
class GeneralInitial2D:
    def __init__(self, input_matrix):
        self.input_matrix = input_matrix
        self.backup_matrix = input_matrix


    def generate_initial_samples(self): 
        if len(self.input_matrix) <= 0:
            self.input_matrix = self.backup_matrix
        print(self.backup_matrix)
        returned_sample = self.input_matrix.pop(0)
        return returned_sample