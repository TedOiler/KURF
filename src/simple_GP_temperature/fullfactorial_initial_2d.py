import pdb

class FullFactorInitial2D:
    def __init__(self, fullfactor_input_list):
        self.fullfactor_input_list = fullfactor_input_list


    def generate_initial_samples(self):
        return_sample = []
        # pdb.set_trace()
        if len(self.fullfactor_input_list) != 0:
            return_sample = self.fullfactor_input_list.pop(0)
        return return_sample