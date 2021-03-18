import pandas as pd
import numpy as np

data = np.random.rand(2, 3, 4)
p = pd.Panel(data)
print(p[0])