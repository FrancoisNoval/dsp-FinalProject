from scipy.signal import butter, lfilter

def butter_bandpass(lowcut, highcut, fs, order=4):
  
    """
    Design a bandpass filter using Butterworth filter.

    Args:
        lowcut (float): Lower cutoff frequency in Hz.
        highcut (float): Higher cutoff frequency in Hz.
        fs (int): Sampling rate in Hz.
        order (int): Order of the filter.

    Returns:
        tuple: Filter coefficients (b, a).
    """
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return b, a

def bandpass_filter(data, lowcut, highcut, fs, order=4):
    """
    Apply a bandpass filter to the given data.

    Args:
        data (list): Input signal data.
        lowcut (float): Lower cutoff frequency in Hz.
        highcut (float): Higher cutoff frequency in Hz.
        fs (int): Sampling rate in Hz.
        order (int): Order of the filter.

    Returns:
        ndarray: Filtered signal.
    """
    b, a = butter_bandpass(lowcut, highcut, fs, order)
    return lfilter(b, a, data)
