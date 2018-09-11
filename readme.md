# Buffon's Needles

## Constants

```python
a = input("a = ");
l = input("l = ");
# a = 3; l = 2;
```

## Prediction of *π*


```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def pi_prediction(a, l, N):
    p = np.array([a*np.random.rand(int(N), 1)\
                  <= l*np.sin(np.pi*np.random.rand(int(N), 1))]).sum()/N;
    return 2*l/(p*a);
```

## Deviation vs. # of Experiments


```python
NmohRange = np.arange(0.01, 0.10, 0.001);
Nrange = np.round(NmohRange**-2);
epsilon = [ ];
for N in Nrange:
    epsilon.append(abs(pi_prediction(a, l, N) - np.pi));
```

## Regression

```python
slope, intercept, r_value, p_value, std_err = stats.linregress(NmohRange, epsilon);
plt.plot(NmohRange, intercept + slope*NmohRange, 'b', label='Fitted line');
```

## Plots

```python
plt.plot(NmohRange, epsilon, 'r.', label = 'Deviation from $\pi$');
plt.legend();
plt.xlabel(r'$\frac{1}{\sqrt{N}}$');
plt.ylabel(r'$\epsilon$');
plt.show();
```

![误差随试验次数收敛][./output_2_0.png]

