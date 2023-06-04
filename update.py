import os
import winreg
import requests
import subprocess
from win10toast import ToastNotifier

# Server URL and local registry key path
server_url = "http://update.troysmithson.com/new.php"
registry_key_path = r"SOFTWARE\AntiVirus"

# Get the current version from the local registry
try:
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, registry_key_path)
    current_version, _ = winreg.QueryValueEx(key, "Version")
    winreg.CloseKey(key)
except WindowsError:
    print("Error: Unable to access the registry key.")
    exit()

# Fetch the latest version from the server
try:
    response = requests.get(server_url)
    latest_version = response.text.strip()
except requests.RequestException:
    print("Error: Failed to retrieve the latest version from the server.")
    exit()

# Compare the versions and update if necessary
if latest_version > current_version:
    # Construct the download URL with the appropriate version
    download_url = f"http://update.troysmithson.com/version/{latest_version}.exe"

    # Download the update executable
    try:
        update_file = requests.get(download_url)
        with open("update.exe", "wb") as file:
            file.write(update_file.content)
    except requests.RequestException:
        print("Error: Failed to download the update.")
        exit()

    # Run the update executable
    update_args = ["/exenoui", "/qn", "/norestart"]
    try:
        subprocess.run(["update.exe"] + update_args, check=True)
    except subprocess.CalledProcessError:
        print("Error: Failed to run the update executable.")
        exit()

    # Send a notification
    toaster = ToastNotifier()
    toaster.show_toast("Update", "Updating")

else:
    print("No updates available.")
