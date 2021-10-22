import pandas as pd

new_dates = ['2021-06-01', '2021-07-01', '2021-08-01', '2021-09-01']
df = pd.read_csv('output/doac_rate_total.csv')
recent_data = df.loc[df['date'].isin(new_dates),:]
recent_data.to_csv("output/doac_rate_total_recent.csv")