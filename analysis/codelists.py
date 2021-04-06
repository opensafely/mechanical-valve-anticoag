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
# The following is a placeholder but should be replaced by above issue
mechanical_valve_codes = codelist_from_csv(
    "codelists/opensafely-valvular-atrial-fibrillation-6cab4902.csv",
    system="ctv3",
    column="code",
)
