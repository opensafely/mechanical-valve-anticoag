from cohortextractor import (
    codelist,
    codelist_from_csv,
)


doac_codes = codelist_from_csv(
    "codelists/opensafely-direct-acting-oral-anticoagulants-doac.csv",
    system="snomed",
    column="id",
)

mecahnical_valve_codes = codelist_from_csv(
    "codelists/xx.csv",
    system="snomed",
    column="id",
)

