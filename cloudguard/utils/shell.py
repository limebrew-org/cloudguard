import subprocess

def execute_command(command:list):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return result

    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        return None