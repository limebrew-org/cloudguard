from modules.provider.gcp.network.firewall import Firewall

if __name__ == '__main__':
    #?: Global Variables
    project_id = "your_project_id"
    credentials = "/path/to/your_service_account_key.json"
    service_account_id = "your-service-account-id"
    
    #? List firewall rules
    firewall_client = Firewall(
        project_id=project_id,
        credentials=credentials,
        service_account_id=service_account_id
    )

    firewall_rules = firewall_client.get_all_firewall_rules()
    print("Firewall Rules: ")
    
    for rule in firewall_rules:
        if "0.0.0.0/0" in rule["sourceRanges"]:
        
            print(f"Name: {rule['name']}")
            print(f"Description: {rule.get('description', 'N/A')}")
            print(f"Source Ranges: {', '.join(rule['sourceRanges'])}")
            print("\n\n")
        
