import os
import json
import pandas as pd
import numpy as np

patients_codes = {}
doac_patients_codes = {}

dates = [
    "input_2019-09-01.csv",
    "input_2019-10-01.csv",
    "input_2019-11-01.csv",
    "input_2019-12-01.csv",
    "input_2020-01-01.csv",
    "input_2020-02-01.csv",
    "input_2020-03-01.csv",
    "input_2020-04-01.csv",
    "input_2020-05-01.csv",
    "input_2020-06-01.csv",
    "input_2020-07-01.csv",
    "input_2020-08-01.csv",
    "input_2020-09-01.csv",
    "input_2020-10-01.csv",
    "input_2020-11-01.csv",
    "input_2020-12-01.csv",
    "input_2021-01-01.csv",
    "input_2021-02-01.csv",
    "input_2021-03-01.csv",
    "input_2021-04-01.csv",
    "input_2021-05-01.csv",

]

patients_list = []
doac_patients_list = []
for file in os.listdir('output'):
        
        if file in dates:
            date = file.split('_')[-1][:-4]

            df = pd.read_csv(os.path.join('output', file))
            
            patients = np.unique(df['patient_id'])
            patients_list.extend(patients)


            doac_subset = df[df['doac']==1]
            doac_patients = patients = np.unique(doac_subset['patient_id'])
            doac_patients_list.extend(doac_patients)


            
unique_patients = len(np.unique(patients_list))
unique_patients_doac = len(np.unique(doac_patients_list))

count_df = pd.DataFrame([['mechanical_valve', unique_patients],['mechanical_valve_doac', unique_patients_doac]], columns=['group','count'])
count_df.to_csv('output/patient_count.csv')
    


