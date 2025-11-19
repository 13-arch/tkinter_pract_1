####################################
import os
import shutil
import sys

exe_name = "my_app.exe"
target_folder = r"D:\MyFolder"

target_path = os.path.join(target_folder, exe_name)

current_exe = sys.executable  

os.makedirs(target_folder, exist_ok=True)

if not os.path.exists(target_path):
    try:
        shutil.copy(current_exe, target_path)
        print(f"{exe_name} скопирован в {target_folder}")
    except Exception as e:
        print(f"Ошибка копирования: {e}")
#######################################