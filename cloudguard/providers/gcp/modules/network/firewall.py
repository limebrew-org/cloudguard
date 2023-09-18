from googleapiclient import discovery
from google.oauth2 import service_account

class Firewall:
    def __init__(self,project_id:str,credentials:str,service_account_id:str):
        self.project_id = project_id
        self.credentials_json = credentials
        self.service_account_id = service_account_id
        self.credentials = service_account.Credentials.from_service_account_file(
            self.credentials_json,
            scopes=['https://www.googleapis.com/auth/cloud-platform']
        )
        self.client = discovery.build('compute','v1',credentials=self.credentials)

    def get_all_firewall_rules(self):
        firewall_rules = self.client.firewalls().list(project=self.project_id).execute()
        return firewall_rules.get('items', [])