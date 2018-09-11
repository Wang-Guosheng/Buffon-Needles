#! /home/wang-guosheng/程序/anaconda3/bin/python

# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# predifined range of N^{-1/2}
NmohRange = np.arange(0.01, 0.10, 0.001);

def pi_prediction(a, l, N):
    """ calculate the prob. that x <= l*sin(theta), then return prediction of pi """
    p = np.array([a*np.random.rand(int(N), 1)\
     <= l*np.sin(np.pi*np.random.rand(int(N), 1))]).sum()/N;
    return 2*l/(p*a);

def calc_dev(a, l, NmohRange):
    """ generate data of epsilon versus N^{-1/2} and plot """
    Nrange = np.round(NmohRange**-2);
    # epsilon = pi_prediction-pi is the deviation of simulated pi value
    epsilon = [ ];
    for N in Nrange:
        epsilon.append(abs(pi_prediction(a, l, N) - np.pi));
    plt.plot(NmohRange, epsilon, 'r.', label = 'Deviation from $pi$');

    # linear regression of epsilon versus N^{-1/2}
    slope, intercept, r_value, p_value, std_err = stats.linregress(NmohRange, epsilon);
    plt.plot(NmohRange, intercept + slope*NmohRange, 'r', label='Fitted line');

    plt.legend();
    plt.xlabel(r'\displaystyle\frac{1}{\sqrt{N}}');
    plt.ylabel(r'\displaystyle\epsilon');
    plt.saveas('buffon_epsilon.png')

if __name__ == "__main__":
    a = float(input("a = "));
    l = float(input("l = "));
    calc_dev(a, l, NmohRange);
