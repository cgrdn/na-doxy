
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import argopy

# specify parameter
param = 'DOXY'

# load BGC index
ix = argopy.ArgoIndex(index_file='bgc-s').load()

for region in [list(Path('../../meta/regions').glob('*.csv'))[1]]:
    
    coords = pd.read_csv(region)
    box = [coords.longitude.min(), coords.longitude.max(), coords.latitude.min(), coords.latitude.max(), 0, 9999]

    # extract box first then polygon
    df = ix.query.compose({
        'box':[coords.longitude.min(), coords.longitude.max(), coords.latitude.min(), coords.latitude.max(), '1995-01-01', '2026-01-01'],
        'params':param,
    }).to_dataframe()

    profiles = pd.DataFrame()
    for i, wmo in enumerate(df.wmo.unique()):
        cycles = df.loc[df.wmo == wmo, 'cyc'].values

        sys.stdout.write(f'loading {cycles.shape[0]} cycles for WMO {wmo} ({i+1}/{df.wmo.unique().shape[0]})...')

        data = argopy.DataFetcher(mode='expert', ds='bgc', params='DOXY').profile(wmo, cycles)
        profiles = pd.concat((profiles, data.to_dataframe()))

        sys.stdout.write('done\n')

        if i > 4:
            break
        