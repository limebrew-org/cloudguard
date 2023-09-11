from modules.utils.shell import execute_command

class IAM:
    def __init__(self,project_id:str,credentials:str,service_account_id:str):
        self.project_id = project_id
        self.credentials = credentials
        self.service_account_id = service_account_id

    def export_all_iam_bindings(self,export_json_file_path:str):
        command = "bash scripts/export_iam_binding.sh {} {} {} {}".format(
        self.project_id,
        self.service_account_id,
        self.credentials,
        export_json_file_path).split(" ")
        execute_command(command)
    
    def get_iam_mapping(self,iam_bindings:list[dict]):
        iam_mapping = {}
        for binding in iam_bindings:
            iam_members = binding["members"]
            iam_role = binding["role"]
            for iam_member in iam_members:
                if iam_member not in iam_mapping.keys():
                    iam_mapping[iam_member] = [iam_role]
                else :
                    iam_mapping[iam_member].append(iam_role)
        return iam_mapping