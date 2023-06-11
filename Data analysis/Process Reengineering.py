import os

def rename_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            new_filename = filename.replace('old_', 'new_')
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

directory_path = 'C:\Users\99450\Documents\GitHub\Python-Projects\Data analysis'
rename_files(directory_path)
