import os
import requests
from hubspot import HubSpot




HUBSPOT_API_KEY = os.getenv("HUBSPOT_API_KEY")
APOLLO_API_KEY = os.getenv("APOLLO_API_KEY")

if (HUBSPOT_API_KEY is None and HUBSPOT_API_KEY == "") or (APOLLO_API_KEY is None and APOLLO_API_KEY == ""):
    raise Exception("Missing API Key(s) in environment variables.")

api_client = HubSpot(access_token=HUBSPOT_API_KEY)
api_client.crm.companies.basic_api.update_with_http_info()



# TODO(ALLAN): Implement
def get_company(company_url : str, company_name : str = None):
    '''
    Takes a company_url, returns the Company Object from Hubspot. If one is not found, a new company is created.

    :param str company_url: The URL of the company website
    :param str company_name: The name of the company

    :return: Company JSON Object
    '''

    # Find company in HubSpot

    # If does not exist, create them in HubSpot

    pass

def lead_enrich(company_url : str):

    # Check if the company_url is a valid domain
    # example.com is valid
    # www.example.com is not
    # allan@example.com is not

    url = str("https://api.apollo.io/api/v1/organizations/enrich?domain=" + company_url)

    headers = {
        "accept": "application/json",
        "Cache-Control": "no-cache",
        "Content-Type": "application/json",
        'x-api-key': APOLLO_API_KEY
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception("Whoa there cowboy! What happened here? " + str(response.text))
    
    res = response.json()
    return res

# TODO(ALLAN): Implement
def add_enriched_data_to_hubspot(data: dict):
    pass

def lambda_handler(event, context):

    # Attempt to extract necessary inputs
    try:
        company_name = event['company_name']
        company_url = event['company_url']

    except Exception as e:
        return {
            'statusCode': 422,
            'Message': str('Unprocessable Entity: ' + str(e))
        }
    
    # AUTHENTICATION

    company = get_company(company_url, company_name=company_name)

    enriched_data = lead_enrich(company)

    # Attach contacts from JSON structure to company
    # -- Search for contact. If exists, use this one and update any info. Else, create contact and use this one
    # -- Attach to the Contacts of the company
    # -- Add to list in HubSpot

    return {
        'statusCode': 200,
        'Message': "Successfully enriched company"
    }


data = {
    "company_name": "Sound Decisions",
    "company_url": "https://sounddecisions.co/"
}


print(lambda_handler(data, None))