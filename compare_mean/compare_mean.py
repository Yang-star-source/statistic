import sys
import numpy as np
import scipy.stats as stats
from tabulate import tabulate

# Force UTF-8 encoding for standard output to support box-drawing characters
sys.stdout.reconfigure(encoding='utf-8')

def t_test_equal_var(xbar1, xbar2,mu1, mu2, s1, s2, n1, n2 , test='two-tailed'):
    """
    Unknown variances, assumed equal (Pooled Variance)
    """

    df1 = n1 - 1
    df2 = n2 - 1
    total_df = df1 + df2
    
    # Calculate the pooled
    S_pooled = np.sqrt(((n1 - 1) * s1**2 + (n2 - 1) * s2**2) / total_df)

    S_xbar1_minus_xbar2 = S_pooled * np.sqrt(1/n1 + 1/n2)

    t_stat = (xbar1 - xbar2 - (mu1 - mu2)) / S_xbar1_minus_xbar2
    
    if test == 'two-tailed':
        p_value = 2 * (1 - stats.t.cdf(abs(t_stat), total_df))

    elif test == 'right':
        p_value = 1 - stats.t.cdf(t_stat, total_df)

    elif test == 'left':
        p_value = stats.t.cdf(t_stat, total_df)
    
    return t_stat, total_df, p_value

def t_test_unequal_var(xbar1, xbar2,mu1, mu2, s1, s2, n1, n2 , test='two-tailed'):
    """
    Unknown variances, assumed unequal
    """

    sigma_x_bar_1_square = s1**2 / n1
    sigma_x_bar_2_square = s2**2 / n2

    df = np.floor((sigma_x_bar_1_square + sigma_x_bar_2_square)**2 / (sigma_x_bar_1_square**2 / (n1 - 1) + sigma_x_bar_2_square**2 / (n2 - 1)))

    t_stat = (xbar1 - xbar2 - (mu1 - mu2)) / np.sqrt(sigma_x_bar_1_square + sigma_x_bar_2_square)

    if test == 'two-tailed':
        p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df))

    elif test == 'right':
        p_value = 1 - stats.t.cdf(t_stat, df)

    elif test == 'left':
        p_value = stats.t.cdf(t_stat, df)
    
    return t_stat, df, p_value

xbar1 = 80
xbar2 = 96
mu1 = 1
mu2 = 1
s1 = 17.5
s2 = 14.4
n1 = 25
n2 = 20

# left , right , two-tailed
test = 'left'

t_stat, df, p_value = t_test_unequal_var(xbar1, xbar2,mu1, mu2, s1, s2, n1, n2 , test=test)
table = [
    ["xbar1", xbar1],
    ["xbar2", xbar2],
    ["mu1", mu1],
    ["mu2", mu2],
    ["s1", s1],
    ["s2", s2],
    ["n1", n1],
    ["n2", n2],
    ["test", test],
    ["t_stat", f"{t_stat:.4f}"],
    ["df", f"{int(df)}"],
    ["p_value", f"{p_value:.4f}"]
]

print(tabulate(table,tablefmt="rounded_grid"))
