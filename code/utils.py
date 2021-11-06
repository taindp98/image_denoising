import numpy as np
import pywt

def add_noisy(img, var=None):
    """
    create a noise array with the same size as the input image
    add noise array into the input image
    """
    row,col= img.shape
    mean = 0
    if not var:
        var = 25
    sigma = var**0.5
    gauss = np.random.normal(mean,sigma,(row,col))
    gauss = gauss.reshape(row,col)
    noisy = img + gauss
    return noisy, gauss

def transform_wavelet(spatial, algo = 'db2'):
    coeffs2 = pywt.dwt2(spatial, algo)
    return coeffs2