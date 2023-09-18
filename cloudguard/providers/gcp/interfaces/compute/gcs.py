from modules.provider.gcp.compute.gcs import CloudStorage

if __name__ == "__main__":

    #?: Global Variables
    project_id = "your_project_id"
    credentials = "/path/to/your_service_account_key.json"
    service_account_id = "your-service-account-id"

    bucket_name = "zoro_assets"

    client = CloudStorage(
        project_id=project_id,
        credentials=credentials,
        service_account_id=service_account_id
    )     

    buckets_list = client.get_all_buckets()
    print()

    for bucket in buckets_list:
        is_public = client.is_bucket_public(bucket_name=bucket.name)

        if is_public:
            print(f"The bucket {bucket.name} is public.")
        else:
            print(f"The bucket {bucket.name} is not public.")