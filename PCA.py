import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

filename4 = 'myTrueAndFalse.txt'
df1 = pd.read_csv(filename4, sep='\t')

X = np.array(df1)
pca = PCA(n_components=3390)
newX = pca.fit_transform(X)

data1 = pd.DataFrame(newX)
data1.to_csv('pcaTrueAndFalse99.txt', sep='\t', index=False)