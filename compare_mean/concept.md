# Comparing mean from 2 different population

Consider we have 2 population groups $P_1$ and $P_2$.

|Population| $P_1$ | $P_2$ |
| --- | --- | ---- |
| Population Mean | $\mu_1$ | $\mu_2$ |
| Population Variance | $\sigma_1^2$ | $\sigma_2^2$ |
| Sample | $S_1$ | $S_2$ |
| Sample Mean | $\bar{x}_1$ | $\bar{x}_2$ |
| Sample Variance | $s_1^2$ | $s_2^2$ |
| Sample Size | $n_1$ | $n_2$ |

Let say we only have information for sample only.
Then 

difference between $2$ means = $\bar{x}_1 - \bar{x}_2$

$$E(\bar{x}_1 - \bar{x}_2) = E(\bar{x}_1) - E(\bar{x}_2) = \mu_1 - \mu_2$$

$$Var(\bar{x}_1 - \bar{x}_2) = Var(\bar{x}_1) + Var(\bar{x}_2)$$

Note that $\sigma_{\bar{x}}^2 = \frac{\sigma^2}{n}$
Then :

$$Var(\bar{x}_1 - \bar{x}_2) = \frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}$$

$$\sigma_{\bar{x}_1 - \bar{x}_2} = \sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}$$

For $n_1 \geq 30$ and $n_2 \geq 30$ , we can apply CLT which approx normal distribution.

$$(\bar{x}_1 - \bar{x}_2) \sim N(\mu_1 - \mu_2, \frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2})$$

$$Z = \frac{value - mean}{std}$$

$$Z = \frac{(\bar{x}_1 - \bar{x}_2) - (\mu_1 - \mu_2)}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}}$$

## If $\sigma_1$ and $\sigma_2$ unknown and assume $\sigma_1 = \sigma_2 = \sigma$
For this case , we sub sample variance to population variance and do $\sigma$ subsitution.

We can sub $\sigma$ in original variance

$$Var(\bar{x}_1 - \bar{x}_2) = \frac{\sigma^2}{n_1} + \frac{\sigma^2}{n_2}$$

$$Var(\bar{x}_1 - \bar{x}_2) = \sigma^2 (\frac{1}{n_1} + \frac{1}{n_2})$$

We have 2 sample variance $s_1^2$ and $s_2^2$ and we knew 2 population variance is same , we need to sub $\sigma$ with new $s$.

Since we have 2 different sample size for the 2 sample , we need to weight it fairly. For example , to avoild sample 1 have 1000 data but sample 2 have only 2 data. We weight it by degree of freedom, $n-1$.

$$new variance = \frac{weight_1 \times s_1^2 + weight_2 \times s_2^2}{total weight}$$

$$w_1 = n_1 - 1$$
$$w_2 = n_2 - 1$$
$$total weight = w_1 + w_2$$

$$new variance = \frac{(w_1 \times s_1^2 + w_2 \times s_2^2)}{w_1 + w_2}$$

$$S_p^2 = \frac{(n_1 - 1) \times s_1^2 + (n_2 - 1) \times s_2^2}{n_1 + n_2 - 2}$$

where $S_p^2$ is pooled variance. Sub $\sigma^2$ with $S_p^2$

$$Var(\bar{x}_1 - \bar{x}_2) = \frac{S_p^2}{n_1} + \frac{S_p^2}{n_2}$$

$$S_{\bar{x}_1 - \bar{x}_2} = S_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}$$

## If $\sigma_1$ and $\sigma_2$ unknown and assume $\sigma_1 \neq \sigma_2$

For this case , substitute population variance with sample variance.

$$S_p^2 = \frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}$$

Use t distribution :

$$t = \frac{(\bar{x}_1 - \bar{x}_2) - (\mu_1 - \mu_2)}{\sqrt{\frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}}}$$

with degree of freedom , df:

$$df = \frac{(\sigma_{\bar{x_1}}^2 + \sigma_{\bar{x_2}}^2)^2}{\frac{(\sigma_{\bar{x_1}}^2)^2}{n_1-1}+\frac{(\sigma_{\bar{x_2}}^2)^2}{n_2-1}}$$

$$df = \frac{(\frac{s_1^2}{n_1} + \frac{s_1^2}{n_1})^2}{\frac{(\frac{s_1^2}{n_1})^2}{n_1-1}+\frac{(\frac{s_1^2}{n_1})^2}{n_2-1}}$$




















