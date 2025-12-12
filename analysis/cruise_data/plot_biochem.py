
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

bc = pd.read_csv('data/extractBioChemData.csv').drop('Unnamed: 0', axis=1)
bc = bc.loc[bc.YEAR > 2020]

g = sns.FacetGrid(bc, col='YEAR', row='PARAMETER_NAME', sharex=False)
g.map(sns.scatterplot, 'DATA_VALUE', 'START_DEPTH')

g.axes[0,0].set_ylim((2050, -50))

plt.show()