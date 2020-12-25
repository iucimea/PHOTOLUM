import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from scipy.signal import find_peaks




spectra_file_names = ['2020-g4/Ti_1V_P0uW_000.txt','2020-g4/Ti_0V_P0uW_001.txt','2020-g4/GaAs_0V_P0uW_002.txt']

labels = ['Ti 1V', 'Ti 0V', 'GaAs 0V'] 

spectra = [pd.read_csv(a, sep=' ') for a in spectra_file_names]

peaks = [find_peaks(a.value2, distance=100, height=10000, prominence=(1000))[0] for a in spectra]


    
for i, a in enumerate(spectra):
    plt.plot(a.wavelength, a.value2, label=labels[i])
    
plt.xlabel('$\lambda$ (nm)')
plt.ylabel('intensity')
plt.legend(loc='best')
plt.savefig('spectra.jpg',dpi=1200)
plt.show()
plt.clf()