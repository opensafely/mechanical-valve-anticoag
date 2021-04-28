import os
import json
import pandas as pd
import numpy as np

patients_list = []
for file in os.listdir('output'):
        
        if file.startswith('input_2'):
            date = file.split('_')[-1][:-4]

            df = pd.read_csv(os.path.join('output', file))
            
            patients = np.unique(df['patient_id'])
            patients_list.append(patients)

            
unique_patients = len(np.unique(patients_list))


with open('output/patient_count.json', 'w') as f:
    json.dump({"num_patients": unique_patients}, f)