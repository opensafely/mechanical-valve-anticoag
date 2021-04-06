from cohortextractor import (
    codelist,
    codelist_from_csv,
)


doac_codes = codelist_from_csv(
    "codelists/opensafely-direct-acting-oral-anticoagulants-doac.csv",
    system="snomed",
    column="id",
)

# https://github.com/opensafely/codelist-development/issues/91
# The following is a placeholder with a DRAFT codelist but should be replaced by above issue
mechanical_valve_codes = codelist_from_csv(
    "codelists/opensafely-mechanical-or-artificial-valves.csv",
    system="snomed",
    column="code",
)
