from modules.provider.gcp.network.dns import CloudDNS
import json


if __name__ == '__main__':
    #?: Global Variables
    project_id = ""
    zone_name = ""
    record_type="A"
    # Initialize the DNS client

    client = CloudDNS(
        project_id=project_id,
        credentials="",
        service_account_id="")

    #?: Get all DNS records
    print("All records: ", json.dumps(client.get_all_records(), indent=6))

    #? Get all DNS records by zone
    print(f"All records for zone: {zone_name}")
    print(json.dumps(client.get_zone_records(zone_name = zone_name), indent=6))



    