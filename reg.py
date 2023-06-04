import winreg

def protect_registry_entry(key_path):
    try:
        # Open the registry key
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_ALL_ACCESS)

        # Set the security descriptor to deny all access to the key
        security_attributes = winreg.QueryInfoKey(key)[6]
        security_attributes |= winreg.KEY_SET_VALUE
        winreg.SetSecurityInfo(key, winreg.SE_OBJECT_TYPE_REGKEY, security_attributes, None, None, None, None)

        # Close the registry key
        winreg.CloseKey(key)

        print("Registry entry protected successfully!")
    except WindowsError as e:
        print("Failed to protect registry entry:", e)

# Example usage: Protecting a specific registry entry
key_path = r"SOFTWARE\Antivirus"
protect_registry_entry(key_path)
