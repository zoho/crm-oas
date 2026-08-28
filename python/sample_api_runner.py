import requests
import logging
import os
from dotenv import load_dotenv

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.configuration import Configuration
from swagger_client.api_client import ApiClient
from swagger_client.api.default_api import DefaultApi

# Use this file for sample testing in your generated SDK file.

# Load environment variables from .env
load_dotenv()

# Configure logging
logging.basicConfig(
    filename='access_token.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Zoho token functions
def get_zoho_crm_access_token():
    # Get Zoho CRM access token
    payload = {
        "refresh_token": os.getenv("REFRESH_TOKEN"),
        "client_id": os.getenv("CLIENT_ID"),
        "client_secret": os.getenv("CLIENT_SECRET"),
        "grant_type": "refresh_token"
    }
    url = "https://accounts.zoho.com/oauth/v2/token"
    response = requests.post(url, data=payload)
    logging.debug("Response body: %s", response.text)
    
    response.raise_for_status()

    print("Zoho Access Token:", response.json().get("access_token"))

def create_refresh_token():
    # Create a refresh token
    payload = {
        "code": os.getenv("CODE"),
        "client_id": os.getenv("CLIENT_ID"),
        "client_secret": os.getenv("CLIENT_SECRET"),
        "redirect_uri": os.getenv("REDIRECT_URI"),
        "grant_type": "authorization_code"
    }
    url = "https://accounts.zoho.com/oauth/v2/token"
    response = requests.post(url, data=payload)
    logging.debug("Create refresh token response: %s", response.text)
    response.raise_for_status()
    return response.json()

def fetch_record(api_instance, module_api_name, record_id):
    try:
        response = api_instance.get_record(module_api_name, record_id)
        print("API response:", response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_record: %s" % e)

def create_new_record(api_instance, module_api_name):
    body = swagger_client.BodyWrapper(
        data=[
            swagger_client.Record(
                Last_Name="Sample Record"
            )
        ]
    )
    try:
        response = api_instance.create_records(body, module_api_name)
        print("Record created:", response)
    except ApiException as e:
        print("Exception when calling DefaultApi->create_records: %s" % e)

def main():
    
    configuration = Configuration()
    configuration.access_token = os.getenv("ACCESS_TOKEN")
    
    api_client = ApiClient(configuration)
    api_instance = DefaultApi(api_client)
    
    # Demonstrate API calls
    # GET Record
  
    module_api_name = 'Leads'
    record_id = 'FAKE_VLAUE'

    fetch_record(api_instance, module_api_name, record_id)

    #POST Record
  
    create_new_record(api_instance, module_api_name,)

if __name__ == "__main__":
    main()
