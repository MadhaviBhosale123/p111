import os
import shutil

from_dir= 'F:/Madhavi Folder'
to_dir = 'F:/Madhavi Folder/Documnet 111'

list_of_files=os.listdir(from_dir)
print(list_of_files)

for i in list_of_files:
    os.path.splitext(to_dir)
    print(i)