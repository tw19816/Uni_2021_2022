from random import sample
import numpy as np
from scipy.stats import chisquare
import matplotlib.pyplot as plt


def pearson_test(sample_data, n_bins, df, func, *args):
    """Test sample data accuracy against model distribution using 
    Pearson's chi-square test.
    
    The sample data is organised in a histogram and compared a model 
    plot using the chi-square distribution to determine how accurately 
    it represents the model data.

    Parameters
    ----------
    sample_data : array_like
        The sample data to be tested. It must contain a 1 dimensional 
        array of datapoints.
    n_bins : int
        The number of bins used to sort the sample data.
    df : int
        The degrees of freedom in the true distribution
    func : function
        The probability density function for the model distribution.
        This function must take the random variable as its first 
        parameter.
    args : float
        Additional arguments required to compute the probability 
        density function. 
    """
    sample_data = np.asarray(sample_data, dtype=float)
    if sample_data.ndim != 1:
        raise ValueError("sample data must be one dimensional")
    # Determine coordinates of the probability density function for the
    # sample data
    bin_prob, bin_edge = np.histogram(sample_data, n_bins, density=True)
    bin_width = bin_edge[1] - bin_edge[0]
    bin_mid = bin_edge[:-1] + bin_mid/2
    del bin_edge, bin_width
    # Determine the coordinates of the probaibilty density function for 
    # the model data
    true_prob = func(bin_mid, *args)
    # Determine ddof: delta degrees of freedom (df-1)
    ddof = df-1
    chi2_stat, p_val = chisquare(bin_prob, true_prob, ddof=ddof)
    return chi2_stat, p_val

