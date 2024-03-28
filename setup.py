from pathlib import Path
import winreg as reg
import sys
import pyuac

def main():
    cpath = Path(sys.argv[0]).resolve().parent

    key_path = r"Directory\\Background\\shell\\WSCM"

    command_key_path = r"{key_path}\\command".format(key_path=key_path)

    key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)
    command_key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, command_key_path)

    reg.SetValue(key, '', reg.REG_SZ, 'Create workspace shortcut in desktop')

    reg.SetValueEx(key, 'Icon', 0, reg.REG_SZ, str(cpath / "data" / "icon.ico"))

    reg.SetValue(command_key, '', reg.REG_SZ, str(cpath / "Release" /"main.exe" ))
if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        pyuac.runAsAdmin()
    else:        
        main()