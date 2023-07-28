from summit import Runner
from summit.benchmarks import SnarBenchmark
from summit.utils.dataset import DataSet

class EvaluationComponentSnar:
    """
    Class for benchmarking Snar
    """
    def __init__(self):
        #The benchmark is from https://github.com/sustainable-processes/summit/tree/main
        #Please check out https://gosummit.readthedocs.io/en/latest/tutorials/intro.html for more info
        self.experiment = SnarBenchmark()

    def __generate_experiment_conditions(self,
                                         residence_time = 0.5,  #minutes [0.5, 2] optimal 0.50
                                         equiv = 2.32,   # [1.0, 5.0] optimal 2.32
                                         concentration = 0.5, #molar [0.1, 0.5] optimal 0.5
                                         temperature = 30.0, #degree celsius [30, 120] optimal 66.23
                                         ):
        """
        Generate a dataframe of experiment conditions
        :return: Pandas dataframe a Pandas dataframe that allows us to specify certain columns as metadata
        """
        columns = [v.name for v in self.experiment.domain.variables ]
        values = {('tau', 'DATA'): residence_time,  # minutes
                  ('equiv_pldn', 'DATA'): equiv,
                  ('conc_dfnb', 'DATA'): concentration,  # molar
                  ('temperature', 'DATA'): temperature,  # degrees celsius
                  }
        conditions = DataSet([values], columns=columns)

        return conditions

    def __reset_experiment(self):
        """
        reset the experiments to reduce the effect of uncontrolled variables
        """
        self.experiment.reset()

    def get_evaluation_score(self,
                        residence_time = 0.5,  #minutes [0.5, 2] optimal 0.50
                        equiv = 2.32,   # [1.0, 5.0] optimal 2.32
                        concentration = 0.5, #molar [0.1, 0.5] optimal 0.5
                        temperature = 30.0, #degree celsius [30, 120] optimal 66.23
                        ):
        """
        Run the experiment with given conditions
        :return: float The result(yield-e_factor) of experiment (round to 2 decimal places)
        """
        self.__reset_experiment()
        conditions = self.__generate_experiment_conditions(residence_time, equiv, concentration, temperature)
        results = self.experiment.run_experiments(conditions)
        results.round(2)
        #result = float(results['sty'] - results['e_factor'])
        result = float(results['sty'])
        return result



