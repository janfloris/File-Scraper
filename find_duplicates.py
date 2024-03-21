import os

class FileObject:
    def __init__(self, name, full_path):
        self.name = name
        self.full_path = full_path

def find_duplicates(root_folder):
    file_only_names = []
    files_to_remove = []
    for foldername, subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            file_extension = os.path.splitext(filename)[1]
            file_only = filename[:-4]
            file_path = os.path.join(foldername, filename)

            if file_only not in file_only_names:
                file_only_names.append(file_only)
            else:
                files_to_remove.append(FileObject(file_only, file_path))
    
    return files_to_remove

if __name__ == "__main__":
    root_folder = r'C:\JF Backup\Arcade\t'
    # root_folder = r'C:\JF Backup\Arcade\RetroPi roms'
    
    duplicate_files = find_duplicates(root_folder)
    
    if duplicate_files:
        print("Duplicate files found:")
        for file_path in duplicate_files:
            print(file_path.full_path)
    else:
        print("No duplicate files found.")

        
