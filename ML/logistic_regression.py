# implementing logistic regression from scratch
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math


def hypothesis(t0, t1, t2, tumor_size, time, i): # putting one training data in the hypothesis
    tx = t0 + t1*tumor_size[i] + t2*time[i]   # Theta_transpose_X
    h = 1/(1+pow(math.e, -tx))
    return h


def cost(t0, t1, t2, m, tumor_size, time, cancer):
    total_c = 0
    for i in range(m):
        # calculating Theta'X
        tx = t0 + t1 * tumor_size[i] + t2 * time[i]
        h = 1/(1+pow(math.e, -tx))
        total_c += (cancer[i]*math.log(h) + (1-cancer[i])*math.log(1-h))
    avg_c = -1*total_c/m
    return avg_c


def step_grad(t0, t1, t2, tumor_size, time, cancer, l, m):
    t0_grad = 0
    t1_grad = 0
    t2_grad = 0
    for i in range(m):
        h = hypothesis(t0, t1, t2, tumor_size, time, i)
        t0_grad += (h-cancer[i])
        t1_grad += (h-cancer[i])*tumor_size[i]
        t2_grad += (h-cancer[i])*time[i]

    nt0 = t0 - l*t0_grad
    nt1 = t1 - l*t1_grad
    nt2 = t2 - l*t2_grad

    return [nt0, nt1, nt2]


def gradient_descent(t0, t1, t2, num_of_iterations, learning_rate, tumor_size, time, cancer, m):
    for _ in range(num_of_iterations):
        t0, t1, t2 = step_grad(t0, t1, t2, tumor_size, time, cancer, learning_rate, m)
    return [t0, t1, t2]


def run():
    data = pd.read_csv('/home/akshay/patients.csv')
    print(data)
    m = len(data)
    print(m)
    tumor_size = [i for i in data.iloc[:, 0]]
    time = [i for i in data.iloc[:, 1]]
    cancer = [i for i in data.iloc[:, 2]]

    learning_rate = 0.001
    theta0 = 0
    theta1 = 0
    theta2 = 0
    num_of_iterations = 10000

    t0, t1, t2 = gradient_descent(theta0, theta1, theta2, num_of_iterations, learning_rate, tumor_size, time, cancer, m)
    print(t0, t1, t2, cost(t0, t1, t2, m, tumor_size, time, cancer))

    # eq. of line is t1x + t2y = -t0
    # where x is tumor_size and y is time
    x1 = [i for i in range(0, 12, 2)]
    y1 = [-(t0+t1*i)/t2 for i in x1]

    # plotting the data on a graph
    plt.scatter(tumor_size, time, label='cancer_or_not')
    plt.plot(x1, y1, 'g', linewidth=2)
    plt.ylabel('time_in_months')
    plt.xlabel('tumor_size')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    run()