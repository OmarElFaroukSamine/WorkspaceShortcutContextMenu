from pathlib import Path
import winreg as reg
import pyuac

from pyuac import main_requires_admin

@main_requires_admin
def main():
    cpath = Path.cwd()

    key_path = r"Directory\\Background\\shell\\WSCM"

    command_key_path = r"{key_path}\\command".format(key_path=key_path)

    key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)
    command_key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, command_key_path)

    reg.SetValue(key, '', reg.REG_SZ, 'Create Workspace shortcut in Desktop')

    reg.SetValueEx(key, 'Icon', 0, reg.REG_SZ, str(cpath / "data" / "icon.ico"))

    reg.SetValue(command_key, '', reg.REG_SZ, str(cpath / "src" / ""))

if __name__ == "__main__":
    main()
