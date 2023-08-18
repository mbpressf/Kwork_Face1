import os

script_path = os.path.abspath(__file__)

dir_path = os.path.dirname(script_path)

image_name = "cutface.jpg"

image_path = os.path.join(dir_path, image_name)

print(image_path)
print(dir_path)
