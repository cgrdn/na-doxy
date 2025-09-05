
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import argopy

# load BGC index
ix = argopy.ArgoIndex(index_file='bgc-s').load()

# select parameter, get some metadata info
param = 'DOXY'
reftbl = argopy.ArgoNVSReferenceTables().tbl('R03')
param_info = reftbl[reftbl['altLabel']==param].iloc[0]

# whether to fetch new data or grab from a previous run
fresh = True



for region in Path('../../meta/regions').glob('scotian*.csv'):
    
    coords = pd.read_csv(region)
    box = [coords.longitude.min(), coords.longitude.max(), coords.latitude.min(), coords.latitude.max(), 0, 9999]

    # extract box first then polygon
    df = ix.query.compose({
        'box':[coords.longitude.min(), coords.longitude.max(), coords.latitude.min(), coords.latitude.max(), '2020-01-01', '2026-01-01'],
        'params':param,
    }).to_dataframe()

    profiles = pd.DataFrame()
    for i, wmo in enumerate(df.wmo.unique()):
        cycles = df.loc[df.wmo == wmo, 'cyc'].values

        sys.stdout.write(f'loading {cycles.shape[0]} cycles for WMO {wmo} ({i+1}/{df.wmo.unique().shape[0]})...')

        data = argopy.DataFetcher(mode='expert', ds='bgc', params=param).profile(wmo, cycles)
        profiles = pd.concat((profiles, data.to_dataframe()))

        sys.stdout.write('done\n')
    
    profiles = profiles.reset_index()

    fig, ax = plt.subplots()
    g = sns.lineplot(
        data=profiles.loc[profiles.DOXY_QC < 4], x='DOXY', y='PRES', 
        hue='PLATFORM_NUMBER', units='CYCLE_NUMBER', 
        palette=sns.dark_palette('dodgerblue'), alpha=0.7,
        orient='y', estimator=None, legend=False,
        ax=ax
    )
    g.axes.set_ylim((2050, -50))

    ax.set_title(f"Profiles of {param_info['prefLabel']} ({param})\n{ix.N_MATCH} profiles ({profiles.PLATFORM_NUMBER.unique().shape[0]} floats) from the {ix.convention_title}")
    fig.savefig(f'figures/{region.name.replace(".csv", "")}_doxy_profiles.png', dpi=350, bbox_inches='tight')
    plt.close(fig)

    fig, axes = plt.subplots(3, 1, sharex=True)
    surf = 50
    surface = profiles.loc[profiles.PRES < surf]
    sns.scatterplot(data=surface, x='TIME', y='TEMP', hue='PLATFORM_NUMBER', palette=sns.dark_palette('crimson'), alpha=0.7, legend=False, ax=axes[0])
    sns.scatterplot(data=surface, x='TIME', y='PSAL', hue='PLATFORM_NUMBER', palette=sns.dark_palette('seagreen'), alpha=0.7, legend=False, ax=axes[1])
    sns.scatterplot(data=surface, x='TIME', y='DOXY', hue='PLATFORM_NUMBER', palette=sns.dark_palette('dodgerblue'), alpha=0.7, legend=False, ax=axes[2])
    plt.show()

    axes[0].set_title(f"Timeseries for the top {surf}m of {param_info['prefLabel']} ({param})\n{ix.N_MATCH} profiles ({df.wmo.unique().shape[0]} floats) from the {ix.convention_title}")
    fig.savefig(f'figures/{region.name.replace(".csv", "")}_timeseries.png', dpi=350, bbox_inches='tight')
    plt.close(fig)