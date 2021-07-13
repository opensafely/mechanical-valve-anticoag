import pandas as pd

import json
df = pd.read_csv('output/input_2021-05-01.csv')

mean_age = df['age'].mean()

with open('output/mean_age.json', 'w') as fp:
    json.dump({
        "age": mean_age,
    }, fp)
