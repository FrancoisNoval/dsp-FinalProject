from scipy.signal import butter, lfilter

def butter_bandpass(lowcut, highcut, fs, order=4):
    """
    Menyusun filter bandpass menggunakan filter Butterworth.
    Args:
        lowcut (float): Frekuensi cutoff bawah dalam Hz.
        highcut (float): Frekuensi cutoff atas dalam Hz.
        fs (int): Frekuensi sampling dalam Hz.
        order (int): Orde filter.
    Returns: 
        tuple: Koefisien filter (b, a).
    """
  
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return b, a

def bandpass_filter(data, lowcut, highcut, fs, order=4):
    """
    Menerapkan filter bandpass pada data yang diberikan.
    
    Args:
        data (list): Data sinyal input.
        lowcut (float): Frekuensi cutoff bawah dalam Hz.
        highcut (float): Frekuensi cutoff atas dalam Hz.
        fs (int): Frekuensi sampling dalam Hz.
        order (int): Orde filter.
        
    Returns:
        ndarray: Sinyal yang telah difilter.
        
    """

    b, a = butter_bandpass(lowcut, highcut, fs, order)
    return lfilter(b, a, data)
