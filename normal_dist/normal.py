import numpy as np
from scipy.stats import norm

# Display easy-readable numbers
np.set_printoptions(suppress=True, precision=4)

def get_z_from_x(x,mean,std):
    z_score = (x-mean)/std
    return z_score

def get_z_from_prob(prob):
    # Right tailed P(Z > z_score)
    # PPF : Percent Point Function , default is left tailed
    prob = 1.0 - prob
    z_score = norm.ppf(prob)
    return z_score

def get_prob_from_x(x,mean,std):
    # Right tailed P(Z > z_score)
    # CDF : Cumulative Density Function , default is left tailed
    prob =1.0 - norm.cdf(x, mean, std)
    return prob

def get_z_critical_from_CI(ci):
    alpha = 1.0 - ci
    z_critic = norm.ppf(1.0 - alpha/2.0)
    return z_critic


# Input
x = 1.96
mean = 0
std = 1
ci = 0.95

z_score = get_z_from_x(x,mean,std)
prob = get_prob_from_x(x,mean,std)
z_critical = get_z_critical_from_CI(ci)

# Output
print(f"Z-score: {z_score:.2f}")
print(f"Probability: {prob:.4f}")
print(f"Get Z from prob: {get_z_from_prob(prob):.2f}")
print(f"Z-critical: {z_critical:.2f}")