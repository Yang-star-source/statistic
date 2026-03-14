import numpy as np
import scipy.stats as stats

def t_test_equal_var(x1_mean, x2_mean, s1_sq, s2_sq, n1, n2):
    """
    Unknown variances, assumed equal (Pooled Variance)
    """
    # Total degrees of freedom
    df = n1 + n2 - 2
    
    # Pooled variance (Sp^2)
    sp_sq = ((n1 - 1) * s1_sq + (n2 - 1) * s2_sq) / df
    
    # Standard error of the difference
    se = np.sqrt(sp_sq * (1/n1 + 1/n2))
    
    # t-statistic
    t_stat = (x1_mean - x2_mean) / se
    
    # Calculate p-value (two-tailed test)
    p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df))
    
    return t_stat, df, p_value

def t_test_unequal_var(x1_mean, x2_mean, s1_sq, s2_sq, n1, n2):
    """
    Unknown variances, assumed unequal (Welch's t-test)
    """
    # Variance of the sample means
    var_x1_mean = s1_sq / n1
    var_x2_mean = s2_sq / n2
    
    # Standard error of the difference
    se = np.sqrt(var_x1_mean + var_x2_mean)
    
    # t-statistic
    t_stat = (x1_mean - x2_mean) / se
    
    # Degrees of freedom (Smith-Satterthwaite formula)
    df_num = (var_x1_mean + var_x2_mean)**2
    df_den = (var_x1_mean**2 / (n1 - 1)) + (var_x2_mean**2 / (n2 - 1))
    df = np.floor(df_num / df_den) 
    
    # Calculate p-value (two-tailed test)
    p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df))
    
    return t_stat, df, p_value