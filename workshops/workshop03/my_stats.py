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
    max_ind = 0
    max_val = 0
    for i in x:
        if i > max_val:
            max_val = i
            max_ind = x[i]  # Doesn't work for numpy array
            

    return max_val, max_ind
