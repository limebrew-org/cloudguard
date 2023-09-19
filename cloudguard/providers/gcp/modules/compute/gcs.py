from google.oauth2 import service_account
from google.cloud import storage

class CloudStorage:
    def __init__(self,project_id:str,credentials:str,service_account_id:str):
        self.project_id = project_id
        self.credentials_json = credentials
        self.service_account_id = service_account_id
        self.credentials = service_account.Credentials.from_service_account_file(
            self.credentials_json,
            scopes=['https://www.googleapis.com/auth/cloud-platform']
        )
        self.client = storage.Client(project=self.project_id,credentials=self.credentials)


    def get_all_buckets(self):
        return self.client.list_buckets()
    
    def is_bucket_public(self, bucket_name:str) -> bool:
        # Get the bucket object
        bucket = self.client.get_bucket(bucket_name)

        
        # Check if the bucket has uniform bucket-level access enabled
        if bucket.iam_configuration.uniform_bucket_level_access_enabled:
            # If uniform bucket-level access is enabled, check IAM policies
            iam_policy = bucket.get_iam_policy()
            
            # Check if there is a role binding that grants read access to allUsers
            for binding in iam_policy.bindings:
                if binding["role"] == "roles/storage.legacyBucketReader" and "allUsers" in binding["members"]:
                    return True
                
        else:
            # If uniform bucket-level access is not enabled, check legacy bucket ACL
            for acl_entry in bucket.acl:
                if acl_entry.get("entity") == "allUsers" and acl_entry.get("role") == "READER":
                    return True

        return False