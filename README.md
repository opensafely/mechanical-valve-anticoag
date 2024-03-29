# Potentially inappropriate prescribing of DOACs to people with mechanical heart valves: a federated analysis of 57.9 million patients’ primary care records in situ using OpenSAFELY

* The published manuscript is available in Thrombosis Research [here](https://doi.org/10.1016/j.thromres.2022.01.023).
* A summary of the work is also available on OpenSAFELY Reports [here](https://reports.opensafely.org/reports/doac-prescribing-in-people-with-a-mechanical-heart-valve-replacement/).
* A self-archived version of the published manuscript is available [here](https://ora.ox.ac.uk/objects/uuid:aa50f867-d3a4-45ff-9173-1c9677a7ba4f).
* Raw model outputs, including charts, crosstabs, etc, are in `released_outputs/`
* If you are interested in how we defined our variables, take a look at the [study definition](analysis/study_definition.py); this is written in `python`, but non-programmers should be able to understand what is going on there
* If you are interested in how we defined our code lists, look in the [codelists folder](./codelists/).
* Developers and epidemiologists interested in the framework should review [the OpenSAFELY documentation](https://docs.opensafely.org)

# About the OpenSAFELY framework

The OpenSAFELY framework is a secure analytics platform for
electronic health records research in the NHS.

Instead of requesting access for slices of patient data and
transporting them elsewhere for analysis, the framework supports
developing analytics against dummy data, and then running against the
real data *within the same infrastructure that the data is stored*.
Read more at [OpenSAFELY.org](https://opensafely.org).
