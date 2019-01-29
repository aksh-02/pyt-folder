from numpy import *
import matplotlib.pyplot as plt


def comp_error(b, m, points):
    tot_error = 0
    for i in range(len(points)):
        tot_error += pow(m*points[i][0]+b-points[i][1],2)

    # calculate avg. error
    avg_error = tot_error/len(points)
    return avg_error


def gradient_descent(points, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m

    for _ in range(num_iterations):
        # update b and m with new more accurate b and m by performing gradient step
        b, m = step_gradient(b, m, array(points), learning_rate)
    return [b, m]


def step_gradient(b, m, points, learning_rate):
    # the below is for partial derivatives
    b_gradient = 0
    m_gradient = 0
    n = len(points)

    for x, y in points:
        b_gradient += (y-(m*x+b))
        m_gradient += (x*(y-(m*x+b)))

    b_gradient = -2*b_gradient/n
    m_gradient = -2*m_gradient/n

    # update b and m values using the above partial derivatives
    new_b = b-learning_rate*b_gradient
    new_m = m-learning_rate*m_gradient

    return [new_b, new_m]


def run():
    # collecting data
    points = genfromtxt('/home/akshay/marks.csv', delimiter=",")
    print(points)

    # defining our hyper parameters, how fast should this model converge
    learning_rate=0.0001

    # y=mx + b
    ini_b = 0
    ini_m = 0
    num_iterations = 100000

    # train our model
    b, m = gradient_descent(points, ini_b, ini_m, learning_rate, num_iterations)

    x = [i for i, j in points]
    y = [j for i, j in points]

    # to plot the line of regression
    xl = [i for i in range(0, 110, 30)]
    yl = [m*i+b for i in xl]

    plt.scatter(x, y, label='marks vs hours', color='c')
    plt.plot(xl, yl, 'g', label='line of regression', linewidth = 2)
    plt.legend()
    plt.ylabel('marks')
    plt.xlabel('hours')
    plt.title('plot')
    plt.show()

    print(b, m, comp_error(b, m, points))


if __name__ == "__main__":
    run()