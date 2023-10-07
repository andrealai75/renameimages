import os, sys
import logging
from datetime import date

logging.basicConfig(
  filename=str(date.today()) + '_rename.log', 
  encoding='utf-8', level=logging.INFO)

from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from renameimages.folder import Folder
MAIN_PATH = "..\\tmp\\Pics\\"

def new_filename(image, index, description):
  return image.get_reference_datetime() + "_" + \
           description + "_" + \
             "[" + str(index).zfill(3) + "].jpg"

def process_sub_folder(folder):
  folder.load_images()
  index = 0
  for image in folder.get_images():
    index += 1
    new_name = folder.path + "\\" + new_filename(image, index, folder.name())
    logging.info("Rollback: ren " + new_name + " " + image.get_image_flename())
    if image.current_name != new_name:
      os.rename(image.current_name, new_name)

def rename():
  print("Renaming the images ...")
  main_folder = Folder(MAIN_PATH)
  main_folder.load_sub_folders()
  for sub_folder in main_folder.get_subfolders():
    process_sub_folder(sub_folder)
  print("Renaming Completed!")