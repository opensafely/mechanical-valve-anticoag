from ast import parse
import pandas as pd
import os
import matplotlib.pyplot as plt

dates = [
    "2019-09-01",
    "2019-10-01",
    "2019-11-01",
    "2019-12-01",
    "2020-01-01",
    "2020-02-01",
    "2020-03-01",
    "2020-04-01",
    "2020-05-01",
    "2020-06-01",
    "2020-07-01",
    "2020-08-01",
    "2020-09-01",
    "2020-10-01",
    "2020-11-01",
    "2020-12-01",
    "2021-01-01",
    "2021-02-01",
    "2021-03-01",
    "2021-04-01",
    "2021-05-01",
]
dates = [pd.to_datetime(x) for x in dates]

emis = pd.read_csv('released_outputs/EMIS/doac_rate_total.csv', parse_dates=['date'], usecols=['population', 'doac', 'date'])
tpp = pd.read_csv('released_outputs/TPP/doac_rate_total.csv', parse_dates=['date'], usecols=['population', 'doac', 'date'])
tpp = tpp[tpp['date'].isin(dates)]

combined = emis.set_index('date').add(tpp.set_index('date'), fill_value=0).reset_index()
combined['rate'] = (combined['doac'] / combined['population']) *1000
combined.to_csv('released_outputs/combined_rate.csv')

def plot_measures(df, title,column_to_plot, filename, y_label='Rate per 1000'):

    
    plt.plot(df['date'], df[column_to_plot])

    plt.ylabel(y_label)
    plt.xlabel('Date')
    plt.ylim(bottom=0, top=df[column_to_plot].max() + df[column_to_plot].max()* 0.1)
    plt.xticks(rotation='vertical')
    plt.title(title)
    plt.tight_layout()
    plt.savefig(f'released_outputs/{filename}.jpeg')
    plt.show()
    
    plt.clf()

plot_measures(combined, 'Number of people with a mechanical valve prescribed a DOAC', 'doac', 'count', y_label = 'Count')
plot_measures(combined, 'Rate of DOAC prescriptions per 1000 patients with a mechanical valve', 'rate', 'rate', y_label = 'Rate per 1000')