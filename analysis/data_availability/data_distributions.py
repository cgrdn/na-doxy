
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import argopy

# load BGC index
ix = argopy.ArgoIndex(index_file='bgc-b').load()

# select parameter, get some metadata info
param = 'DOXY'
reftbl = argopy.ArgoNVSReferenceTables().tbl('R03')
param_info = reftbl[reftbl['altLabel']==param].iloc[0]

# select profiles in north atlantic with param
df = ix.query.compose({
    'box':[-80, 0, 20, 90, '1995-01-01', '2026-01-01'],
    'params':param,
}).to_dataframe()

# extract data mode
df['variables'] = df['parameters'].apply(lambda x: x.split())
df[f'{param}_data_mode'] = df.apply(lambda x: x['parameter_data_mode'][x['variables'].index(param)] if param in x['variables'] else '', axis=1)
df['year'] = df['date'].apply(lambda x: x.year)

# plot distributions
g = sns.histplot(df, x='year', hue=f'{param}_data_mode', multiple='stack', bins=np.arange(2000, 2026)+0.5)
g.figure.savefig('figures/year_histplot.png', bbox_inches='tight', dpi=350)
plt.close(g.figure)

g = sns.histplot(df, x='latitude', hue=f'{param}_data_mode', multiple='stack', bins=np.arange(20, 95, 5))
g.figure.savefig('figures/latitude_histplot.png', bbox_inches='tight', dpi=350)
plt.close(g.figure)