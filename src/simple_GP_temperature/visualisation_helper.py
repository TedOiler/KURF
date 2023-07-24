import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def scatter_diagram_3d(data_dict):
    """
    generate a 3D scatter diagram with input dictionary
    :param data_dict: Dict{(float, float): float} A dictionary with 2d tuple key and 1d value
    """
    # separate the dictionary into three lists for plotting
    x1_values = [key[0] for key in data_dict.keys()]
    x2_values = [key[1] for key in data_dict.keys()]
    z_values = list(data_dict.values())

    # create the plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # plot the data
    ax.scatter(x1_values, x2_values, z_values)

    # add labels if desired
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.set_zlabel('Z')

    plt.show()

def function_visualisation_3d(func):
    """
    Visualise a input 2d function in rang -10 to 10
    :param func: A function to be visualised
    """
    x1 = np.linspace(-10, 10, 100)
    x2 = np.linspace(-10, 10, 100)

    X1, X2 = np.meshgrid(x1, x2)
    Z = func(X1, X2)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X1, X2, Z)

    plt.show()

def scatter_diagram_colour_3d(data_dict):
    """
    Generate a 2d scatter diagram with colour showing the Z value for 3d data
    :param data_dict: Dict{(float, float): float} A dictionary with 2d tuple key and 1d value
    """
    # separate the dictionary into three lists for plotting
    x1_values = [key[0] for key in data_dict.keys()]
    x2_values = [key[1] for key in data_dict.keys()]
    z_values = list(data_dict.values())

    # create the plot
    fig, ax = plt.subplots()

    # plot the data using color to represent the z-values
    scatter = ax.scatter(x1_values, x2_values, c=z_values)

    # create a colorbar
    fig.colorbar(scatter)

    # set labels if desired
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')

    plt.show()

def line_chart_3d(data_dict):
    """
    Generate a 2d line chart of values at each iteration for 3d input dictionary
    :param data_dict: Dict{(float, float): float} A dictionary with 2d tuple key and 1d value
    """
    # separate the dictionary into two lists for plotting
    x_values = range(0, len(data_dict.keys()))
    y_values = list(data_dict.values())

    # create the plot
    plt.figure(figsize=(10, 6))

    # plot the data
    plt.plot(x_values, y_values, marker='o')

    # set labels if desired
    plt.xlabel('Iteration Number')
    plt.ylabel('Values')
    plt.title('Values at each iteration')

    plt.show()