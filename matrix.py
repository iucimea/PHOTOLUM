import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



voltages=np.arange(-1.5,1.02,0.02)

matrix = pd.read_csv('matrix_indexed.txt', sep=" ")



plt.imshow(matrix,aspect='auto',origin='lower')
plt.savefig('matrix.png',dpi=300)
plt.show()