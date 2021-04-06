from cohortextractor import StudyDefinition, measure, patients, codelist, codelist_from_csv


study = StudyDefinition(
	index_date="2021-03-31",
    # Configure the expectations framework
    default_expectations={
        "date": {"earliest": "2020-01-01", "latest": "today"},
        "rate": "exponential_increase",
        "incidence" : 0.2
    },

    population_denom = patients.satisfying(
    	"""registered 
    	AND
        (NOT has_died) 
        AND
        age>=16 AND age <= 120 
        AND
        mechanical_valve
        """),

    registered = patients.registered_as_of(
    	"index_date",
        return_expectations={"incidence": 0.9},),

    has_died=patients.died_from_any_cause(
        on_or_before=index_date,
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
        mecahnical_valve_codes,
        on_or_before=index_date,
        returning="binary_flag",
        return_expectations={"incidence": 0.01,},
    ),


    doac=patients.with_these_medications(
        doac_codes,
        between=["index_date - 3 months", "index_date"],
        return_expectations={"incidence": 0.2},
    ),

     # stp is an NHS administration region based on geography
    stp=patients.registered_practice_as_of(
        index_date,
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


measures = [
    Measure(
        id = "doac_rx_mecahnical_valve",
        numerator = "doac",
        denominator = "population_denom",
        group_by = "stp",
    ),
]