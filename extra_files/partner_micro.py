import requests
data_category = "10-K Cash"
if data_category == "10-K Cash":
    # get company concept/Assets data
    companyConcept = requests.get(
        (
            f'https://data.sec.gov/api/xbrl/companyconcept/CIK{cik_str}'
            f'/us-gaap/Cash.json'
        ),
        headers=headers
    )