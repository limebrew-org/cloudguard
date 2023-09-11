import os
from googleapiclient import discovery
from google.oauth2 import service_account

# Replace with your project ID and service account key file path
PROJECT_ID = 'your_project_id'
SERVICE_ACCOUNT_KEY_FILE = '/path/to/your_service_account_key.json'

# Initialize the Compute Engine API client
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_KEY_FILE,
    scopes=['https://www.googleapis.com/auth/cloud-platform']
)

compute_service = discovery.build('compute', 'v1', credentials=credentials)

def list_firewall_rules(project_id:str) -> list(dict):
    firewall_rules = compute_service.firewalls().list(project=project_id).execute()
    return firewall_rules.get('items', [])


if __name__ == '__main__':
    try:
        project_id = PROJECT_ID
        
        #? List firewall rules
        firewall_rules = list_firewall_rules(project_id)
        print("Firewall Rules: ")
        
        for rule in firewall_rules:
            print(rule)
            print(f"Name: {rule['name']}")
            print(f"Description: {rule.get('description', 'N/A')}")
            print(f"Source Ranges: {', '.join(rule['sourceRanges'])}")
            print(f"Allowed Protocols and Ports: {', '.join(rule['allowed'][0]['ports'])}\n")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
