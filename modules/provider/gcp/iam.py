from modules.utils.shell import execute_command

class IAM:
    def __init__(self,project_id:str,credentials:str,service_account_id:str):
        """
        #? Constructor that sets project_id and credentials for authentication with google cloud
        """
        self.project_id = project_id
        self.credentials = credentials
        self.service_account_id = service_account_id

    def export_all_iam_bindings(self,export_json_file_path:str):
        """
        #? This method will run gcloud cli and will export all IAM bindings
        #? for a google cloud project

        Input:
        export_json_file_path: path where the exported IAM bindings will be saved (in json format)

        Functionality:
        It splits the command in " " and is provided input to execute_command function which exports all IAM bindings

        Output:
        Return None
        """
        command = "bash scripts/export_iam_binding.sh {} {} {} {}".format(
        self.project_id,
        self.service_account_id,
        self.credentials,
        export_json_file_path).split(" ")
        execute_command(command)
    
    def get_iam_mapping(self,iam_bindings:list[dict]):
        """
        #? This method creates a mapping between IAM members and their associated roles.

        Input:
        iam_bindings: List of IAM bindings (a list of dictionary) 
        where each element is a dictionary consisting of IAM members
        associated with a particular IAM role

        Functionality:
        Loop over iam_bindings and set the member as a key to the dictionary and put the role as a value which is a list

        Output:
        Returns a hashmap (dictionary) consisting of keys as IAM members and values as IAM roles
        """
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