import os
import requests

os.getenv("HUBSPOT_API_KEY")


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

def lead_enrich(company_object : object):
    # Pass whole Company Object from HubSpot into Lead Enrichment Module
    headers = {

    }
    data = {

    }

    requests.post("some URL of a provider that does lead enrichment", headers=headers, payload=data)

    pass

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

    lead_enrich(company)

    '''
    Return the following structure

    Contacts: [
        {
            firstName,
            lastName,
            email,
            phone,
            title,
            data: [
                # additional fields that may or may not exist depending on lead enrichment source
            ]
        }
    ]
    # Company: {
    #     ...
    # }
    '''

    # Attach contacts from JSON structure to company
    # -- Search for contact. If exists, use this one and update any info. Else, create contact and use this one
    # -- Attach to the Contacts of the company
    # -- Add to list in HubSpot

    return {
        'statusCode': 200,
        'Message': "Successfully enriched company"
    }