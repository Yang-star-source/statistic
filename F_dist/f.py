from scipy.stats import f

def get_prob_from_f(f_score,df1,df2):
    # Right tailed
    prob = 1.0 - f.cdf(f_score, df1, df2)
    return prob

def get_f_from_prob(prob,df1,df2):
    # Right tailed
    prob = 1.0 - prob
    f_score = f.ppf(prob, df1, df2)
    return f_score

def get_f_critical_from_CI(ci,df1,df2):
    alpha = 1.0 - ci
    f_critical = f.ppf(1.0 - alpha/2.0, df1, df2)
    return f_critical

# Input
f_score = get_f_from_prob(0.01,1,1)
df1 = 1
df2 = 1
ci = 0.95

# Output
print(f"F-score: {f_score:.3f}")
print(f"Probability: {get_prob_from_f(f_score,df1,df2):.4f}")
print(f"F-critical: {get_f_critical_from_CI(ci,df1,df2):.3f}")