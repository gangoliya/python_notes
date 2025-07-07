# Directory & File Management

# os.mkdir(), os.remove(), os.rename()
import os, shutil
os.mkdir("backup")
os.rename("python_teaching/file_handling/image_1.jpg", "python_teaching/file_handling/image.jpg")
os.remove("image_1.txt")



# shutil.copy(), shutil.remtree()
shutil.copy("file.txt", "backup/file.txt")
# shutil.rmtree("my_folder")