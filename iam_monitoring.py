import json
import subprocess
import os

def load_json(filename):
    with open(filename, 'r') as file:
        exported_json = json.load(file)
    file.close()
    return exported_json

def build_mapping (iam_bindings):
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

def execute_command(command:list):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return result

    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        return None
    
def export_iam(project_id, export_json_path):
    command = f"bash export_iam.sh {project_id} {export_json_path}"
    execute_command(command = command.split(" "))  

def delete_file(file_path):
    try:
        os.remove(file_path)
    except FileNotFoundError:
        print(f"{file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def rename_file(current_file_path, new_file_path):      
    try:
        os.rename(current_file_path, new_file_path)
    except FileNotFoundError:
        print(f"{current_file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    #?: Global Variables
    project_id = "first-project-394615"
    export_json_prev_path = "iam_permissions_prev.json"
    export_json_curr_path = "iam_permissions_curr.json"


    #?: Export iam_bindiings for a project and export it in json
    export_iam(project_id=project_id, export_json_path=export_json_curr_path)

    #?: Load json
    exported_json_prev = load_json(export_json_prev_path)
    exported_json_curr = load_json(export_json_curr_path)

    #?: Get IAM bindings
    prev_bindings = exported_json_prev["bindings"]
    curr_bindings = exported_json_curr["bindings"]

    #?: Build mapping between members and roles
    prev_map = build_mapping(iam_bindings=prev_bindings)
    curr_map = build_mapping(iam_bindings=curr_bindings)

    #? Compare the 2 dictionaries to find the changes
    prev_set = set(prev_map.keys())
    curr_set = set(curr_map.keys())

    iam_members_created = curr_set - prev_set
    iam_members_deleted = prev_set - curr_set

    if len(iam_members_created) > 0 or len(iam_members_deleted) > 0:

        if len(iam_members_created) > 0:
            print("iam_members_created", iam_members_created)
        if len(iam_members_deleted) > 0:
            print("iam_members_deleted", iam_members_deleted)
        print("\n\n")

    iam_members_common = prev_set.intersection(curr_set)

    for iam_member in list(iam_members_common):
        prev_roles = prev_map[iam_member]
        curr_roles = curr_map[iam_member]

        prev_roles_set = set(prev_roles)
        curr_roles_set = set(curr_roles)

        roles_created = curr_roles_set - prev_roles_set
        roles_deleted = prev_roles_set - curr_roles_set

        if len(roles_created) > 0 or len(roles_deleted) > 0:
            print("iam_member", iam_member)

            if len(roles_created) > 0:
                print("roles_created", roles_created)

            if len(roles_deleted) > 0:
                print("roles_deleted", roles_deleted)
                
            print("\n\n")


    delete_file(file_path=export_json_prev_path)
    rename_file(current_file_path=export_json_curr_path, new_file_path=export_json_prev_path)






