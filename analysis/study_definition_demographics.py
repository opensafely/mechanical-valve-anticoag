from cohortextractor import (
    StudyDefinition,
    patients,
    codelist,
    codelist_from_csv,
)
from codelists import *



study = StudyDefinition(
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
    index_date="2021-04-01",

## Medication
      doac=patients.with_these_medications(
        doac_codes,
        on_or_before="index_date - 3 months",
        return_expectations={"incidence": 0.2},
    ),


## Mechanical Valve

      mechanical_valve=patients.with_these_clinical_events(
                mechanical_valve_codes,
                on_or_before="index_date",
                returning="binary_flag",
                return_expectations={"incidence": 0.01,},
            ),


## Demographics



    # Index of multiple deprivation
    imd=patients.address_as_of(
        "index_date",
        returning="index_of_multiple_deprivation",
        round_to_nearest=100,
        return_expectations={
            "category": {
                "ratios": {
                    "1": 0.2,
                    "6001": 0.2,
                    "12001": 0.2,
                    "18001": 0.2,
                    "24001": 0.2,
                }
            },
        },
    ), 

    # Patients in long-stay nursing and residential care
    longres_dat=patients.with_these_clinical_events(
        codelists.longres,
        returning="date",
        find_last_match_in_period=True,
        on_or_before="index_date",
        date_format="YYYY-MM-DD",
    ),

    # Ethnicity
    eth2001=patients.with_these_clinical_events(
        codelists.eth2001,
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
    # Any other ethnicity code
    non_eth2001_dat=patients.with_these_clinical_events(
        codelists.non_eth2001,
        returning="date",
        find_last_match_in_period=True,
        on_or_before="index_date",
        date_format="YYYY-MM-DD",
    ),
    # Ethnicity not given - patient refused
    eth_notgiptref_dat=patients.with_these_clinical_events(
        codelists.eth_notgiptref,
        returning="date",
        find_last_match_in_period=True,
        on_or_before="index_date",
        date_format="YYYY-MM-DD",
    ),
    # Ethnicity not stated
    eth_notstated_dat=patients.with_these_clinical_events(
        codelists.eth_notstated,
        returning="date",
        find_last_match_in_period=True,
        on_or_before="index_date",
        date_format="YYYY-MM-DD",
    ),
    # Ethnicity no record
    eth_norecord_dat=patients.with_these_clinical_events(
        codelists.eth_norecord,
        returning="date",
        find_last_match_in_period=True,
        on_or_before="index_date",
        date_format="YYYY-MM-DD",
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
)

