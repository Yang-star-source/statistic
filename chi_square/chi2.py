from scipy.stats import chi2

def get_prob_from_chi2(chi2_score,df):
    # Right tailed 
    prob = 1.0 - chi2.cdf(chi2_score, df)
    return prob

def get_chi2_from_prob(prob,df):
    # Right tailed
    prob = 1.0 - prob
    chi2_score = chi2.ppf(prob, df)
    return chi2_score

def get_chi2_critical_from_CI(ci,df):
    alpha = 1.0 - ci
    chi2_critical = chi2.ppf(1.0 - alpha/2.0, df)
    return chi2_critical

# Input
chi2_score = get_chi2_from_prob(0.1,1)
df = 1
ci = 0.95

# Output
print(f"Chi2-score: {chi2_score:.3f}")
print(f"Probability: {get_prob_from_chi2(chi2_score,df):.4f}")
print(f"Chi2-critical: {get_chi2_critical_from_CI(ci,df):.3f}")