import os
import glob
import shutil

# specify the path of the folder where the files are located
folder_path = os.path.join(os.path.expanduser('~'), 'Downloads')

# get a list of all files in the folder
files = glob.glob(os.path.join(folder_path, '*'))

# sort the list of files by modification time
files.sort(key=os.path.getmtime)

# get the latest file
latest_file = files[-1]

script_path = os.path.abspath(__file__)
destination_folder= os.path.dirname(script_path)

# specify the new file name
new_file_name = 'face_download.jpg'

# move and rename the file
shutil.move(latest_file, os.path.join(destination_folder, new_file_name))
