import os
import json
import pandas as pd
import numpy as np

patients_codes = {}
doac_patients_codes = {}
recent_doac_patients_codes = {}

patients_list = []
for file in os.listdir('output'):
        
        if file.startswith('input_2'):
            date = file.split('_')[-1][:-4]

            df = pd.read_csv(os.path.join('output', file))
            
            patients = np.unique(df['patient_id'])
            patients_list.extend(patients)


            def get_patient_valve_code(row, output_dict):
                patient = row['patient_id']
                code = row['mechanical_valve_code']
                output_dict[patient] = code
            
            df.apply(lambda row: get_patient_valve_code(row, patients_codes), axis=1)


            doac_subset = df[df['doac']==1]
            doac_subset.apply(lambda row: get_patient_valve_code(row, doac_patients_codes), axis=1)

            # if last 3 months get separate count

            if date in ['2021-04-01', '2021-03-01', '2021-02-01']:
                doac_subset.apply(lambda row: get_patient_valve_code(row, recent_doac_patients_codes), axis=1)

            
unique_patients = len(np.unique(patients_list))


with open('output/patient_count.json', 'w') as f:
    json.dump({"num_patients": unique_patients}, f)

with open('output/patient_valve_codes.json', 'w') as f:
    json.dump({"num_patients": patients_codes}, f)

with open('output/patient_doac_valve_codes.json', 'w') as f:
    json.dump({"num_patients": doac_patients_codes}, f)

with open('output/recent_patient_doac_valve_codes.json', 'w') as f:
    json.dump({"num_patients": recent_doac_patients_codes}, f)