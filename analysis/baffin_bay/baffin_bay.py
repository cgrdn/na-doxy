
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import argopy
argopy.set_options(mode='expert')

import gsw

# box defining Baffin Bay and Davis Strait
box = [-80, -50, 66, 77]
# dates, entire argo era
dates = ['2025-01-01', '2026-01-01']
# data selections requires depths, select entire water column
depth = [0, 9999]

# select data, depth limits to select all data
params = ['TEMP', 'PSAL', 'DOXY', 'CHLA', 'BBP700', 'PH_IN_SITU_TOTAL', 'NITRATE']
data = argopy.DataFetcher(ds='bgc-s', parallel=True, params='all').region(box + depth + dates).load()
df = data.to_dataframe()
ix = data.index

# map profiles, show year
argopy.plot.scatter_map(
    ix,
    hue='wmo',
    cmap='Spectral_r',
    padding=(5, 5)
)

plt.savefig('figures/profiles_map_month.png', bbox_inches='tight', dpi=300)
plt.close()

fig, axes = plt.subplots(3, 2, sharex=True)
depth_ranges = [[0, 100], [100, 500], [500, 3000]]
titles = ['PRES < 100 dbar', '100 dbar < PRES < 500 dbar', 'PRES > 500 dbar']
for i, v in enumerate(['TEMP', 'DOXY']):
    axcol = axes[:,i]
    for ax, dr, title in zip(axcol, depth_ranges, titles):
        legend = i == 0 and dr[0] == 0
        sub = df.loc[(df.PRES > dr[0]) & (df.PRES < dr[1])]
        sns.scatterplot(data=sub, x='TIME', y=v, hue='PLATFORM_NUMBER', s=1, alpha=0.25, palette='colorblind', ax=ax, legend=False)
        sns.lineplot(data=sub, x='TIME', y=v, hue='PLATFORM_NUMBER', palette='colorblind', ax=ax, legend=legend)

        if v == 'TEMP':
            ax.set_title(title)

for ax in axes[-1,:]:
    # customize tick labels
    ax.set_xticks([tick + 15 for tick in ax.get_xticks()], minor=True)
    ax.set_xticklabels([pd.Timestamp(year=2025, month=int(tick.get_text().split('-')[1]), day=1).strftime('%b')[0] for tick in ax.get_xticklabels()], minor=True)

for ax in axes[-1,:]:
    ax.set_xticklabels('')

ticks = ax.get_xticks()
ax.set_xlim(right=ticks[-1] + 30)
ax.set_xticks(ticks)

fig.set_size_inches(1.5*fig.get_figwidth(), 1.5*fig.get_figheight())
fig.savefig('figures/TEMP_DOXY_timeseries_2025.png', bbox_inches='tight', dpi=300)

df['SA'] = gsw.SA_from_SP(df['PSAL'], df['PRES'], df['LONGITUDE'], df['LATITUDE'])
df['CT'] = gsw.CT_from_t(df['SA'], df['TEMP'], df['PRES'])
df['O2sol'] = gsw.O2sol(df['SA'], df['CT'], df['PRES'], df['LONGITUDE'], df['LATITUDE'])
df['AOU'] = df['O2sol'] - df['DOXY']

params = ['CT', 'SA', 'DOXY', 'O2sol', 'AOU']
units = {
    'PRES':'dbar',
    'CT':f'{chr(176)}C',
    'SA':'g kg$^{-1}$',
    'DOXY':'$\mathregular{\mu}$mol kg$^{-1}$',
    'O2sol':'$\mathregular{\mu}$mol kg$^{-1}$',
    'AOU':'$\mathregular{\mu}$mol kg$^{-1}$',
}

fig, axes = plt.subplots(1, len(params), sharey=True)
for v, ax in zip(params, axes):
    sns.lineplot(data=df, x=v, y='PRES', hue='PLATFORM_NUMBER', units='TIME', orient='y', estimator=None, palette='colorblind', alpha=0.5, ax=ax, legend=v == 'AOU')
    ax.set_xlabel(f'{ax.get_xlabel()} ({units[ax.get_xlabel()]})')
ax.set_ylim((1025, -25))
axes[0].set_ylabel(f'{ax.get_ylabel()} ({units[ax.get_ylabel()]})')
axes[-1].axvline(0, color='k', ls='--')

fig.set_size_inches(len(params)/2*fig.get_figwidth(), fig.get_figheight())
fig.savefig('figures/TEMP_DOXY_profiles_2025.png', bbox_inches='tight', dpi=300)