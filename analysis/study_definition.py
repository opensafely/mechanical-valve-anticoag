from cohortextractor import (
    StudyDefinition,
    Measure,
    patients
)
from codelists import *

study = StudyDefinition(
    index_date="2021-05-01",
    
    # Configure the expectations framework
    default_expectations={
        "date": {"earliest": "2020-01-01", "latest": "today"},
        "rate": "exponential_increase",
        "incidence": 0.2,
    },
    population=patients.satisfying(
        """registered 
    	AND
        (NOT has_died) 
        AND
        age>=16 AND age <= 120 
        AND
        mechanical_valve
        """,

            registered=patients.registered_as_of(
                "index_date", return_expectations={"incidence": 0.9},
            ),
            has_died=patients.died_from_any_cause(
                on_or_before="index_date",
                returning="binary_flag",
                return_expectations={"incidence": 0.05},
            ),
           
   ),
    

    # stp is an NHS administration region based on geography
    stp=patients.registered_practice_as_of(
        "index_date",
        returning="stp_code",
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "STP1": 0.1,
                    "STP2": 0.1,
                    "STP3": 0.1,
                    "STP4": 0.1,
                    "STP5": 0.1,
                    "STP6": 0.1,
                    "STP7": 0.1,
                    "STP8": 0.1,
                    "STP9": 0.1,
                    "STP10": 0.1,
                }
            },
        },
    ),
    
    
    
    age=patients.age_as_of(
                "index_date",
                return_expectations={
                    "rate": "universal",
                    "int": {"distribution": "population_ages"},
                },
            ),
    
    age_band=patients.categorised_as(
        {
            "0": "DEFAULT",
            "0-19": """ age >= 0 AND age < 20""",
            "20-29": """ age >=  20 AND age < 30""",
            "30-39": """ age >=  30 AND age < 40""",
            "40-49": """ age >=  40 AND age < 50""",
            "50-59": """ age >=  50 AND age < 60""",
            "60-69": """ age >=  60 AND age < 70""",
            "70-79": """ age >=  70 AND age < 80""",
            "80+": """ age >=  80 AND age < 120""",
        },
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "0": 0.001,
                    "0-19": 0.124,
                    "20-29": 0.125,
                    "30-39": 0.125,
                    "40-49": 0.125,
                    "50-59": 0.125,
                    "60-69": 0.125,
                    "70-79": 0.125,
                    "80+": 0.125,
                }
            },
        },
    ),
    
    imd=patients.categorised_as(
        {
            "0": "DEFAULT", 
            "1": """index_of_multiple_deprivation >=1 AND index_of_multiple_deprivation < 32844*1/5""",
            "2": """index_of_multiple_deprivation >= 32844*1/5 AND index_of_multiple_deprivation < 32844*2/5""",
            "3": """index_of_multiple_deprivation >= 32844*2/5 AND index_of_multiple_deprivation < 32844*3/5""",
            "4": """index_of_multiple_deprivation >= 32844*3/5 AND index_of_multiple_deprivation < 32844*4/5""",
            "5": """index_of_multiple_deprivation >= 32844*4/5 AND index_of_multiple_deprivation < 32844""",
        },
        index_of_multiple_deprivation=patients.address_as_of(
            "index_date",
            returning="index_of_multiple_deprivation",
            round_to_nearest=100,
        ),
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "0": 0.05,
                    "1": 0.19,
                    "2": 0.19,
                    "3": 0.19,
                    "4": 0.19,
                    "5": 0.19,
                }
            },
        },
    ),
    
    sex=patients.sex(
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"M": 0.49, "F": 0.5, "U": 0.01}},
        }
    ),
    
    atrial_fib=patients.with_these_clinical_events(
        af_codes,
        on_or_before="index_date",
        returning="binary_flag",
        return_expectations={"incidence": 0.01,},
    ),
    

    mechanical_valve=patients.with_these_clinical_events(
                mechanical_valve_codes,
                on_or_before="index_date",
                returning="binary_flag",
                return_expectations={"incidence": 0.01,},
            ),
    
    mechanical_valve_code =patients.with_these_clinical_events(
                mechanical_valve_codes,
                on_or_before="index_date",
                returning="code",
                return_expectations={"category": {
            "ratios": {174920003: 1}}, },
            ),
    
    
    
    doac=patients.with_these_medications(
        doac_codes,
        between=["index_date", "last_day_of_month(index_date)"],
        return_expectations={"incidence": 0.2},
    ),

    doac_code=patients.with_these_medications(
        doac_codes,
        between=["index_date", "last_day_of_month(index_date)"],
        returning="code",
        return_expectations={"category": {
            "ratios": {19506911000001105: 1}}, },
    ),
    
    doac_3_months = patients.with_these_medications(
        doac_codes,
        between=["index_date - 2 months", "last_day_of_month(index_date)"],
        return_expectations={"incidence": 0.2},
    ),

)

measures = [
    Measure(
        id="doac_rx_mechanical_valve_rate",
        numerator="doac",
        denominator="population",
        group_by="stp",
    ),


    Measure(
        id="doac_rx_mechanical_valve_3_month_rate",
        numerator="doac_3_months",
        denominator="population",
        group_by="stp",
    ),
    
    Measure(
        id="doac_rx_mechanical_valve_3_month_sex_rate",
        numerator="doac_3_months",
        denominator="population",
        group_by="sex",
    ),
    
    Measure(
        id="doac_rx_mechanical_valve_3_month_imd_rate",
        numerator="doac_3_months",
        denominator="population",
        group_by="imd",
    ),
    
    Measure(
        id="doac_rx_mechanical_valve_3_month_af_rate",
        numerator="doac_3_months",
        denominator="population",
        group_by="atrial_fib",
    ),


    Measure(
        id="doac_rx_mechanical_valve_3_month_ethnicity_rate",
        numerator="doac_3_months",
        denominator="population",
        group_by="eth2001",
    ),
    
    Measure(
        id="doac_rx_mechanical_valve_3_month_age_rate",
        numerator="doac_3_months",
        denominator="population",
        group_by="age_band",
    ),
    
    Measure(
        id="doac_rx_mechanical_valve_3_month_valve_code_rate",
        numerator="doac_3_months",
        denominator="population",
        group_by="mechanical_valve_code",
    ),
    
    Measure(
        id="stp_rate",
        numerator="doac",
        denominator="population",
        group_by="stp",
    ),

    Measure(
        id="doac_code_rate",
        numerator="doac",
        denominator="population",
        group_by="doac_code",
    ),

   

   
]
