import os
import subprocess
import urllib.request

def download_psexec(psexec_path):
    download_url = 'https://live.sysinternals.com/psexec.exe'
    try:
        urllib.request.urlretrieve(download_url, psexec_path)
        print('psexec.exe downloaded successfully.')
    except Exception as e:
        print(f'Error downloading psexec.exe: {e}')

def run_as_system(file_paths):
    psexec_directory = r'C:\Program Files\Antivirus'
    psexec_path = os.path.join(psexec_directory, 'psexec.exe')

    # Check if psexec.exe exists in the specified directory
    if not os.path.exists(psexec_path):
        # Download psexec.exe if it's not found
        download_psexec(psexec_path)

    for file_path in file_paths:
        cmd = [psexec_path, '-s', '-i', '-d', '-accepteula', file_path]

        try:
            subprocess.run(cmd, check=True)
            print(f'Successfully executed {file_path} as system.')
        except subprocess.CalledProcessError as e:
            print(f'Error executing {file_path} as system: {e}')

# Usage example
files_to_run = [
    r'C:\path\to\file1.exe',
    r'C:\path\to\file2.exe',
    r'C:\path\to\file3.exe'
]  # Specify the paths to the files you want to run
run_as_system(files_to_run)
