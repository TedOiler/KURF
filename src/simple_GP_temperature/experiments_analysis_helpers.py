from matplotlib import pyplot as plt
import numpy as np

def generate_improvement_curve_list(data_dict, start_index):
    """
    Function for converting the input dictionary into a list for improvement curve that starts from the given index
    param: data_dict: {(double, double): double} the input dictionary that consists of the input values as key and the output value as its dictionary value.
    param: start_index: int the starting index of input dictionary 
    return: list[double] a list of values for the improvement curve
    """
    #convert the dictionary to a list of items, sorted by the keys 
    data_list = sorted(list(data_dict.items()))
    result_curve = []
    result_curve.append(data_list[start_index][1])
    for i in range(start_index,len(data_list)-1):
        if data_list[i][1] > result_curve[-1]:
            # add the value to the list only when the value is better than previous one
            result_curve.append(data_list[i][1])
        else: result_curve.append(result_curve[-1])
    return result_curve

def generate_improvement_curve_diagram(mappings_lst, start_idx):   
    """
    The functuion for generating the improvement curve
    param: mappings_lst: [{(double, double): double}] A list of the input dictionaries 
    param:start_idx: int the starting index of input dictionary (for the fucntion generate_improvement_curve_list)
    """
    improve_iter_num_lst = []
    for local_opt_mappings in mappings_lst:
        improve_iter_num_lst.append(generate_improvement_curve_list(local_opt_mappings, start_index = start_idx))

    x_value=range(len(improve_iter_num_lst[0]))
    for i, y_values in enumerate(improve_iter_num_lst):
        if len(y_values) < len(x_value):
            temp = len(improve_iter_num_lst[0])
            while len(y_values) < len(x_value):
                temp = temp - 1
                x_value=range(temp)
        if len(y_values) > len(x_value):
            while len(y_values) > len(x_value):
                y_values.pop()
        plt.plot(x_value, y_values, linestyle='--', label=f'Data {i+1}',color = 'skyblue')

    plt.title('improvement curve')
    plt.xlabel('number of iterations')
    plt.ylabel('improved result')
    plt.show()

def greatest_value(data_dict):
    #convert the dictionary to a list of items, sorted by the keys 
    data_list = sorted(list(data_dict.items()))
    result_curve = data_list[0][1]
    for i in range(0,len(data_list)-1):
        if data_list[i][1] > result_curve:
            result_curve = data_list[i][1]
        else: result_curve = result_curve
    return result_curve

def greatest_number_of_iter(data_dict):
    #convert the dictionary to a list of items, sorted by the keys 
    data_list = sorted(list(data_dict.items()))
    temp = data_list[0][1]
    current_best_iter = 0
    for i in range(0,len(data_list)-1):
        if data_list[i][1] > temp:
            temp = data_list[i][1]
            current_best_iter = i
        else: temp = temp
    return current_best_iter

def greatest_number_of_iter_with_start_idx(data_dict, start_idx):
    #convert the dictionary to a list of items, sorted by the keys 
    data_list = sorted(list(data_dict.items()))
    temp = data_list[0][1]
    current_best_iter = start_idx
    for i in range(start_idx,len(data_list)-1):
        if data_list[i][1] > temp:
            temp = data_list[i][1]
            current_best_iter = i
        else: temp = temp
    return current_best_iter

def best_value_mean(experiments_results):
    experiments_mean_values = {}
    for exp_name, exp_results in experiments_results.items(): 
        best_values = []
        for exp in exp_results:
            best_value  = greatest_value(exp)
            best_values.append(best_value)
        best_values = np.array(best_values)
        experiments_mean_values[exp_name] = best_values.mean()
    return experiments_mean_values

def best_iter_mean(experiments_results):
    # the iteration that gets the best evaluation value
    experiments_mean_iters = {}
    for exp_name, exp_results in experiments_results.items(): 
        best_values = []
        for exp in exp_results:
            best_value  = greatest_number_of_iter(exp)
            best_values.append(best_value)
        best_values = np.array(best_values)
        experiments_mean_iters[exp_name] = best_values.mean(), best_values.std()
    return experiments_mean_iters

def get_best_evlauation_scores(experiment_list):
    best_value_list = []
    for exp_set in experiment_list:
        best_value = greatest_value(exp_set)
        best_value_list.append(best_value)
    return best_value_list

def get_best_iter(experiment_list):
    best_iter_list = []
    for exp_set in experiment_list:
        best_iter = greatest_number_of_iter(exp_set)
        best_iter_list.append(best_iter)
    return best_iter_list

def get_best_iter_with_start_idx(experiment_list, start_idx):
    best_iter_list = []
    for exp_set in experiment_list:
        best_iter = greatest_number_of_iter_with_start_idx(exp_set, start_idx)
        best_iter_list.append(best_iter)
    return best_iter_list