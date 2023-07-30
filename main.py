from BO_GP_temperature import BOTemperatureGP
from evaluation_component import EvaluationComponentSnar
from random_initial import RandomInit
#import wandb

def main():
    ev = EvaluationComponentSnar()
    init = RandomInit(30.0, 120.0)
    # wandb.login()
    # wandb.init(
    #     project='BO_GP_temperature',
    #     name=f'total iter: {250} number of initial samples: {2}',
    #     config = {
    #             'total_iter': 250,
    #             'num_of_init': 2,
    #             },
    # )
    bayes_opt = BOTemperatureGP(evaluation_component=ev, initial_method=init)
    mappings = bayes_opt.optimise()
    # print(f'mappings {mappings}')
    best_temp = max(mappings, key=lambda key:mappings[key])
    print(f'The best is temperature {best_temp[0]} degree celsius')

if __name__ == '__main__':
    main()