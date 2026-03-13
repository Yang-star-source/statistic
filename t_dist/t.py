from scipy.stats import t
import numpy as np

def get_prob_from_t(t_score,df):
    # Right tailed
    prob = 1.0 - t.cdf(t_score, df)
    return prob

def get_t_from_prob(prob,df):
    # Right tailed
    prob = 1.0 - prob
    t_score = t.ppf(prob, df)
    return t_score

def get_t_critical_from_CI(ci,df):
    alpha = 1.0 - ci
    t_critical = t.ppf(1.0 - alpha/2.0, df)
    return t_critical

# Input
t_score = get_t_from_prob(0.1,1)
df = 1
ci = 0.95

# Output
print(f"T-score: {t_score:.3f}")
print(f"Probability: {get_prob_from_t(t_score,df):.4f}")
print(f"T-critical: {get_t_critical_from_CI(ci,df):.3f}")