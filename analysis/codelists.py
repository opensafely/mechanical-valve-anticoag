from cohortextractor import (
    codelist,
    codelist_from_csv,
)

doac_codes = codelist_from_csv(
    "codelists/opensafely-direct-acting-oral-anticoagulants-doac.csv",
    system="snomed",
    column="id",
)

# Metal Valve https://github.com/opensafely/codelist-development/issues/91
mechanical_valve_codes = codelist_from_csv(
    "codelists/opensafely-mechanical-or-artificial-valves.csv",
    system="snomed",
    column="code",
)

# NHSD AF list
af_codes = codelist_from_csv(
    "codelists/nhsd-primary-care-domain-refsets-afib_cod.csv",
    system="snomed",
    column="code",
)

# Ethnicity codes
eth2001 = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-eth2001.csv",
    system="snomed",
    column="code",
    category_column="grouping_16_id",
)

# Any other ethnicity code
non_eth2001 = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-non_eth2001.csv",
    system="snomed",
    column="code",
)

# Ethnicity not given - patient refused
eth_notgiptref = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-eth_notgiptref.csv",
    system="snomed",
    column="code",
)

# Ethnicity not stated
eth_notstated = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-eth_notstated.csv",
    system="snomed",
    column="code",
)

# Ethnicity no record
eth_norecord = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-eth_norecord.csv",
    system="snomed",
    column="code",
)

self_monitoring_code = codelist(["309901000000107"], system="snomed")

inr_blood_testing_codes = codelist_from_csv(
    "codelists/opensafely-inr_blood_testing_reagents.csv",
    system="snomed",
    column="dmd_id",
)
