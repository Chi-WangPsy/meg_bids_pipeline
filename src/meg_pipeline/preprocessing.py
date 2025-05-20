def bandpass_filter(raw, l_freq=1.0, h_freq=40.0):
    return raw.copy().filter(l_freq=l_freq, h_freq=h_freq)
