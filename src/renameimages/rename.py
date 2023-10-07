import os, sys

from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from renameimages.folder import Folder
MAIN_PATH = "c:\\Andrea\\Fotografie\\PIC\\tmp\\Pics\\"

def rename():
  main_folder = Folder(MAIN_PATH)
  main_folder.load_sub_folders()
  for folder in main_folder.get_subfolders():
    folder.load_images()
    index = 0
    for image in folder.get_images():
      index += 1
      print(image)
      new_name = image.get_reference_datetime() + "_" + \
        os.path.basename(folder.get_path()) + "_" + \
          "[" + str(index).zfill(3) + "].jpg"
      print("\t - New Name: " + new_name)