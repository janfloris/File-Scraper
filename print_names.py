import os

folder_path = r'C:\JF Backup\Arcade\RetroPi roms\nes'  # Replace with the actual folder path

for filename in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, filename)):
        print(filename)
