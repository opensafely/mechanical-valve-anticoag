import pandas as pd
import json

start_df = pd.read_csv('output/input_valve_replacement_2020-05-01.csv')
end_df = pd.read_csv('output/input_valve_replacement_2020-05-01.csv')

aortic_valve_codes = [174929002, 275199000, 275200002, 275201003, 275202005, 736892002, 736893007, 860667004, 125411000119107] 

start_num = len(start_df[start_df['mechanical_valve_code'].isin(aortic_valve_codes)])
end_num = len(end_df[end_df['mechanical_valve_code'].isin(aortic_valve_codes)])



with open('output/aortic_valve_count.json', 'w') as fp:
    json.dump({
        "start": start_num,
        "end": end_num
    }, fp)
