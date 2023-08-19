import os
import glob
import shutil

folder_path = os.path.join(os.path.expanduser('~'), 'Downloads')
files = glob.glob(os.path.join(folder_path, '*'))
files.sort(key=os.path.getmtime)
latest_file = files[-1]
script_path = os.path.abspath(__file__)
destination_folder= os.path.dirname(script_path)
new_file_name = 'face_download.jpg'

shutil.move(latest_file, os.path.join(destination_folder, new_file_name))
