import os

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

def isFileExist(file_path):
    return os.path.isfile(file_path)