
# A Python function that checks the peaks in an array and returns a list of indices of those peaks

def find_peaks(peaks):
    stored_peaks = []
    for i in range(1,len(peaks)-1):
        if((peaks[i] > peaks[i-1]) & (peaks[i] > peaks[i + 1])):
            stored_peaks.append(i)
     return stored_peaks       
  

