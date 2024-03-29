import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
def is_overweight(weight, height):

    bmi = round(weight / ((height / 100) ** 2))
    if bmi > 25:
        return 1
    return 0

df['overweight'] = df.apply(lambda x: is_overweight(x['weight'], x['height']),axis=1)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestrol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

#Convert to binary
def converter (c):
    if int(c) >= 2:
        return 1
    return 0

df['cholesterol'] = df.apply(lambda x: converter(x['cholesterol']),axis=1)
df['gluc'] = df.apply(lambda x: converter(x['gluc']),axis=1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'glucose', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df.melt(id_vars=['cardio'], value_vars=['cholesterol', 'gluc',	'smoke', 'alco',	'active', 'overweight'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    df_cat = pd.DataFrame(df_cat.groupby(['cardio',	'variable',	'value'])['value'].count())
    df_cat.rename(columns={'value': 'total'}, inplace=True)
    df_cat.reset_index(inplace=True)
    # Draw the catplot with 'sns.catplot()'

    catplot = sns.catplot(
      data=df_cat,
      kind='bar',
      x='variable',
      y='total',
      hue='value',
      col='cardio')
    fig = catplot.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():

    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                  (df['weight'] >= df['weight'].quantile(0.025)) &
                  (df['weight'] <= df['weight'].quantile(0.975)) &
                  (df['height'] >= df['height'].quantile(0.025)) &
                  (df['height'] <= df['height'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 12))

    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(
        corr,
        mask=mask,
        square=True,
        annot=True,
        linewidths=0.5,
        fmt='.1f',
        center=0,
        vmin=-0.1,
        vmax=0.25,
        cbar_kws={
            'shrink': .45,
            'format': '%.2f'
        })

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig