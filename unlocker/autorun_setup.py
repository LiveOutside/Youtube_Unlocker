import winreg


# Add to autorun
def add_to_startup(program_name, executable_path):
    """
    Adds executable/batch file to autorun through Regedit
    """
    # Reg
    registry_path = winreg.HKEY_CURRENT_USER
    key_path = r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"
    
    try:
        # Opening key to write in Reg
        with winreg.OpenKeyEx(registry_path, key_path, 0, winreg.KEY_WRITE) as registry_key:
            # Create/update Reg
            winreg.SetValueEx(registry_key, program_name, 0, winreg.REG_SZ, executable_path)
        print(f": Success, {program_name} added to autorun.")
        
    except PermissionError:
        print("!! Permission Error: Run script as Admin")
        
# Check for programm to work as autorun programm
def check_startup_entry(program_name):
    """
    Checks if file in autorun using Reg
    """
    registry_path = winreg.HKEY_CURRENT_USER
    key_path = r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"
    
    try:
        # Opening key to read from Reg
        with winreg.OpenKeyEx(registry_path, key_path, 0, winreg.KEY_READ) as registry_key:
            program_path, regtype = winreg.QueryValueEx(registry_key, program_name)
        print(f"!? Trouble, {program_name} already added to autorun, path: {program_path}")
        
    except FileNotFoundError:
        print(f"!! Error, {program_name} not found in autorun.")