from cohortextractor import StudyDefinition, Measure, patients
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
            "index_date",
            return_expectations={"incidence": 0.9},
        ),
        has_died=patients.died_from_any_cause(
            on_or_before="index_date",
            returning="binary_flag",
            return_expectations={"incidence": 0.05},
        ),
    ),
    age=patients.age_as_of(
        "index_date",
        return_expectations={
            "rate": "universal",
            "int": {"distribution": "population_ages"},
        },
    ),
    monitoring=patients.with_these_clinical_events(
        monitoring_codes,
        on_or_before="index_date",
        returning="binary_flag",
        return_expectations={
            "incidence": 0.01,
        },
    ),
    mechanical_valve=patients.with_these_clinical_events(
        mechanical_valve_codes,
        on_or_before="index_date",
        returning="binary_flag",
        return_expectations={
            "incidence": 0.01,
        },
    ),
)

measures = [
    Measure(
        id="monitoring_mechanical_valve_rate",
        numerator="monitoring",
        denominator="population",
        group_by="population",
    ),
]
