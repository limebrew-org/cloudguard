from modules.provider.gcp.network.dns import CloudDNS
import json


if __name__ == '__main__':
    #?: Global Variables
    project_id = "your_project_id"
    credentials = "/path/to/your_service_account_key.json"
    service_account_id = "your-service-account-id"
    zone_name = "your_dns_zone_name"
    record_type="your_record_type"
    record_name="your_record_name"
    
    #?: Initialize the DNS client
    client = CloudDNS(
        project_id=project_id,
        credentials=credentials,
        service_account_id=service_account_id)

    #?: Get all DNS records
    print("All records: ", json.dumps(client.get_all_records(), indent=6))

    #? Get all DNS records by zone_name
    print(f"All records for zone: {zone_name}")
    print(json.dumps(client.get_zone_records(zone_name = zone_name), indent=6))

    #? Get all DNS records by zone_name and record_type
    print(f"All records for zone: {zone_name} and record_type: {record_type}")
    print(json.dumps(client.get_zone_records_by_type(zone_name =zone_name, record_type =record_type), indent=6))

    #? Get all DNS records by zone_name and record_name
    print(f"All records for zone: {zone_name} and record_name: {record_name}")
    print(json.dumps(client.get_zone_records_by_name(zone_name =zone_name, record_name =record_name), indent=6))
    