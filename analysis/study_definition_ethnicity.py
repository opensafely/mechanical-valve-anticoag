from cohortextractor import (
    StudyDefinition,
    patients,
    codelist,
    codelist_from_csv,
    Measure,
)

from datetime import date


end_date = "2021-05-01"

from codelists import *

study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": "today"},
        "rate": "uniform",
    },
    index_date=end_date,
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
            age=patients.age_as_of(
                "index_date",
                return_expectations={
                    "rate": "universal",
                    "int": {"distribution": "population_ages"},
                },
            ),
        mechanical_valve=patients.with_these_clinical_events(
                mechanical_valve_codes,
                on_or_before="index_date",
                returning="binary_flag",
                return_expectations={"incidence": 0.01,},
            ),
           
   ),

    # Ethnicity
    eth2001=patients.with_these_clinical_events(
        eth2001,
        returning="category",
        find_last_match_in_period=True,
        on_or_before="index_date",
        return_expectations={
            "category": {
                "ratios": {
                    "1": 0.5,
                    "2": 0.25,
                    "3": 0.125,
                    "4": 0.0625,
                    "5": 0.03125,
                    "6": 0.015625,
                    "7": 0.0078125,
                    "8": 0.0078125,
                }
            },
            "rate": "universal",
        },
    ),


)