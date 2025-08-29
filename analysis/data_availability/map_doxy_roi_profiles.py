
from pathlib import Path

import pandas as pd
import shapely

import matplotlib.pyplot as plt
import argopy

# load BGC index
ix = argopy.ArgoIndex(index_file='bgc-b').load()

# select parameter, get some metadata info
param = 'DOXY'
reftbl = argopy.ArgoNVSReferenceTables().tbl('R03')
param_info = reftbl[reftbl['altLabel']==param].iloc[0]

for region in Path('regions').glob('*.csv'):
    coords = pd.read_csv(region)
    polygon = shapely.Polygon(coords)

    # extract box first then polygon
    df = ix.query.compose({
        'box':[coords.longitude.min(), coords.longitude.max(), coords.latitude.min(), coords.latitude.max(), '1995-01-01', '2026-01-01'],
        'params':param,
    }).to_dataframe()
    # extract data mode
    df['variables'] = df["parameters"].apply(lambda x: x.split())
    df[f'{param}_data_mode'] = df.apply(lambda x: x['parameter_data_mode'][x['variables'].index(param)] if param in x['variables'] else '', axis=1)

    # more specific polygon subset
    df = df.loc[[polygon.contains(shapely.Point(x, y)) for x, y in zip(df.longitude, df.latitude)]]

    # plot trajectories, color by data mode
    fig, ax, _ = argopy.plot.scatter_map(
        df,
        hue=f'{param}_data_mode',
        cmap='data_mode',
        traj=True,
        legend_title=f'{param} data mode',
        markersize=5,
    )

    fig.savefig(f'figures/{region.name.replace(".csv", "")}_doxy_profiles_map.png', bbox_inches='tight', dpi=350)
    plt.close(fig)

