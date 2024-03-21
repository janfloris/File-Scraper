import os
import shutil
import zipfile
des_folder_path = r'C:\JF Backup\Arcade\t\extracted'  # Replace with the actual folder path
folder_path = r'C:\JF Backup\Arcade\t'

for file_name in os.listdir(folder_path):
    if file_name.endswith('.zip'):
        file_path = os.path.join(folder_path, file_name)
        # shutil.copy(file_path, des_folder_path)
        with zipfile.ZipFile(os.path.join(folder_path, file_name), 'r') as zip_ref:
            zip_ref.extractall(des_folder_path)



