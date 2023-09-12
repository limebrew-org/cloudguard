from modules.utils.json import load_json
from modules.utils.file import delete_file, rename_file, isFileExist
from modules.provider.gcp.iam_admin.iam import IAM


if __name__ == "__main__":
    #?: Global Variables
    project_id = "your_project_id"
    export_json_prev_path = "exports/iam_permissions_prev.json"
    export_json_curr_path = "exports/iam_permissions_curr.json"
    credentials = "/path/to/your_service_account_key.json"
    service_account_id = "your-service-account-id"

    #? Initialize IAM module
    iam = IAM(
        project_id=project_id,
        credentials=credentials,
        service_account_id=service_account_id
    )

    #? Check whether prev json path exists
    if not isFileExist(export_json_prev_path):
        #?: Export iam_bindiings for a project and export it in json
        iam.export_all_iam_bindings(export_json_file_path=export_json_prev_path)
        print("Exported IAM bindings for the first run! Next processes skipped. Rerun again to see the changes")
        exit()


    #?: Export iam_bindiings for a project and export it in json
    iam.export_all_iam_bindings(export_json_file_path=export_json_curr_path)

    #?: Load json
    exported_json_prev = load_json(export_json_prev_path)
    exported_json_curr = load_json(export_json_curr_path)

    #?: Get IAM bindings
    prev_bindings = exported_json_prev["bindings"]
    curr_bindings = exported_json_curr["bindings"]

    #?: Build mapping between members and roles
    prev_map = iam.get_iam_mapping(iam_bindings=prev_bindings)
    curr_map = iam.get_iam_mapping(iam_bindings=curr_bindings)

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
            print("iam_member: ", iam_member)

            if len(roles_created) > 0:
                print("roles_created: ", roles_created)

            if len(roles_deleted) > 0:
                print("roles_deleted: ", roles_deleted)
                
            print("\n\n")


    delete_file(file_path=export_json_prev_path)
    rename_file(current_file_path=export_json_curr_path, new_file_path=export_json_prev_path)