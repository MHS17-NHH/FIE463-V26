from math import sqrt


def my_std(x):
    '''
    Compute and generate the standard deviation of a sequence x

    Parameters
    -----------
    x : Sequence or array

    Returns
    --------
    std : float
        Standard deviation of values in x
    ''' 
    # Step 1: Mean of x
    x_bar = sum(x) / len(x)
    # Step 2: Mean of squared x (List comprehension to square elements of x)
    S = sum(i**2 for i in x) / len(x)
    # Step 3: Variance
    var = S - x_bar**2
    # Step 4: Standard deviation
    std = sqrt(var)

    return std


def my_argmax(x):
    '''
    Docstring for my_argmax
    
    :param x: Description
    '''
    imax = 0
    xmax = 0
    for i, xi in enumerate(x[1:]):
        if xi > xmax:
            imax = i
            xmax = xi  
            

    return imax
