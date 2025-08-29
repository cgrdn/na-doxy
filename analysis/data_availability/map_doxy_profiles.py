
import matplotlib.pyplot as plt
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
df['variables'] = df["parameters"].apply(lambda x: x.split())
df[f'{param}_data_mode'] = df.apply(lambda x: x['parameter_data_mode'][x['variables'].index(param)] if param in x['variables'] else '', axis=1)

# plot trajectories, color by data mode
fig, ax, _ = argopy.plot.scatter_map(
    df,
    hue=f'{param}_data_mode',
    cmap='data_mode',
    traj=True,
    legend_title=f'{param} data mode',
    markersize=5,
)

# title
ax.set_title(f"Data mode for '{param_info['prefLabel']}' ({param})\n{ix.N_MATCH} profiles ({df.wmo.unique().shape[0]} floats) from the {ix.convention_title}")

# save figure
fig.savefig('figures/na_ocean_doxy_profiles_map.png', bbox_inches='tight', dpi=350)
plt.close(fig)