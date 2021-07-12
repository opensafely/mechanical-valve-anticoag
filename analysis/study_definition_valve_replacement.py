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
        """
        mechanical_valve
        """,    
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
            "ratios": {174929002: 1}}, },
            ),

)

