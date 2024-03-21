import os
import re
import os
import re
import re

folder_path = r'C:\JF Backup\Arcade\t\snes'  # Replace with the actual folder path
#folder_path = r'C:\JF Backup\Arcade\RetroPi roms\nes'



# spaces between abbreviations
#string_to_replace = r' by.*?\.'
# string_to_replace = r'\s\[!\]'
# string_to_replace = r'\.\.'
string_to_replace = r','
replace_with = ''
counter = 1

for filename in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, filename)):
                
        new_filename = re.sub(string_to_replace, replace_with, filename)

        new_file_path = os.path.join(folder_path, new_filename)
        if os.path.exists(new_file_path) and filename != new_filename:
            # os.remove(os.path.join(folder_path, new_filename))
            new_file_path = os.path.join(folder_path, '00 - ' + new_filename)
            if os.path.exists(new_file_path):
                os.remove(os.path.join(folder_path, new_filename))
            os.rename(os.path.join(folder_path, filename), new_file_path)
        else :    
            os.rename(os.path.join(folder_path, filename), new_file_path)