import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

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


emis = pd.read_csv('released_outputs/EMIS/doac_rate_total.csv', usecols=['population', 'doac', 'date'])
tpp = pd.read_csv('released_outputs/TPP/doac_rate_total.csv', usecols=['population', 'doac', 'date'])
tpp = tpp[tpp['date'].isin(dates)]
emis = emis[emis['date'].isin(dates)]

combined = emis.set_index('date').add(tpp.set_index('date'), fill_value=0).reset_index()
combined['rate'] = (combined['doac'] / combined['population']) *1000

combined.to_csv('released_outputs/combined_rate.csv')

combined = emis.set_index('date').add(tpp.set_index('date'), fill_value=0).reset_index()
combined['rate'] = (combined['doac'] / combined['population']) *1000
combined.to_csv('released_outputs/combined_rate.csv')

# combined['date'] = pd.to_datetime(combined['date'])
# fortnight = [i + pd.DateOffset(weeks=2) for i in combined['date']]
# for i in fortnight:
#     combined = combined.append({'date': i}, ignore_index=True)

# combined = combined.sort_values('date')
# combined['date'] = combined['date'].dt.strftime('%Y-%m-%d')

def plot_measures(df, title,column_to_plot, filename, y_label='Rate per 1000'):

    df.plot.bar('date',column_to_plot, legend=False)
#     plt.plot(df['date'], df[column_to_plot])

    plt.ylabel(y_label)
    plt.xlabel('Date')
    plt.ylim(bottom=0, top=df[column_to_plot].max() + df[column_to_plot].max()* 0.1)
    plt.xticks(rotation='vertical')
   
    plt.title(title, size=10)
    plt.tight_layout()
    plt.savefig(f'released_outputs/{filename}.jpeg')
    plt.show()
    
    plt.clf()

plot_measures(combined, 'Number of people with coded as having a mechanical valve prescribed a DOAC', 'doac', 'count', y_label = 'Count')
plot_measures(combined, 'Rate of DOAC prescriptions per 1000 patients coded as having a mechanical valve', 'rate', 'rate', y_label = 'Rate per 1000')


subset_1 = combined.loc[combined['date'].isin(['2019-09-01','2019-10-01', '2019-11-01','2019-12-01', '2020-01-01', '2020-02-01']),'doac']
subset_2 = combined.loc[combined['date'].isin(['2020-03-01', '2020-04-01', '2020-05-01', '2020-06-01', '2020-07-01', '2020-08-01']),'doac']


def poisson_ci(series):
    total = np.sum(series)
 
    ci = 1.96*(np.sqrt(total)/len(series))
    return ci


def plot_measures_with_means(df, title,column_to_plot, filename, mean_1, mean_2, y_label='Rate per 1000'):

    
#     plt.plot(df['date'], df[column_to_plot])
    plt.bar(df['date'],height=df['doac'])

    plt.ylabel(y_label)
    plt.xlabel('Date')
    plt.ylim(bottom=450, top=600)
    plt.xticks(rotation='vertical')
    plt.title(title)
    plt.tight_layout()

  
  
    ci_1 = poisson_ci(subset_1)    
    ci_2 = poisson_ci(subset_2)
 
    
    plt.plot(['2019-09-01','2019-10-01','2019-11-01','2019-12-01', '2020-01-01', '2020-02-01'],[mean_1]*6, color='black')
    plt.plot(['2020-03-01', '2020-04-01', '2020-05-01', '2020-06-01', '2020-07-01', '2020-08-01'], [mean_2]*6, color='black')
 
    plt.errorbar(2.5, mean_1, yerr=ci_1,
        c='red', ls='none', capsize=4)
    
    plt.errorbar(8.5, mean_2, yerr=ci_2,
        c='red', ls='none', capsize=4)
    
    plt.show()
    plt.savefig(f'released_outputs/{filename}.jpeg')
    plt.clf()

plot_measures_with_means(combined, 'Number of people coded as having a mechanical valve prescribed a DOAC', 'doac', 'count_with_mean', y_label = 'Count', mean_1=np.mean(subset_1), mean_2=np.mean(subset_2))
