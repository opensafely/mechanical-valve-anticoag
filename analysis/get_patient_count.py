import os
import json
import pandas as pd
import numpy as np

patients_codes = {}
doac_patients_codes = {}


patients_list = []
doac_patients_list = []
for file in os.listdir('output'):
        
        if file.startswith('input_2'):
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
    


