import os, sys
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime
import logging

from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

class Img:
  def __init__(self, current_name):
    self.current_name = current_name
    self.date_taken = self.get_date_taken_datetime()
    self.date_filename = self.extract_data_filename()
    self.file_created = self.get_file_created()
    self.reference_datetime = self.get_datetime_formatted()

  def get_image_flename(self):
    return os.path.basename(self.current_name)

  def get_reference_datetime(self):
    return self.reference_datetime

  def get_date_taken_str(self):
    image = Image.open(self.current_name)
    exifdata = image.getexif()
    for tag_id in exifdata:
      tag = TAGS.get(tag_id, tag_id)
      if tag == "DateTime":
        return exifdata.get(tag_id)

  def get_date_taken_datetime(self):
    try:
      full_text = self.get_date_taken_str()
      return datetime.strptime(full_text, '%Y:%m:%d %H:%M:%S')
    except:
      logging.warning(self.get_image_flename() + " - Missing Data Taken")
      return None

  def extract_data_filename(self):
    try:
      file = self.get_image_flename()
      data_substring = file[1:15]
      return datetime.strptime(data_substring, '%Y%m%d_%H%M%S')
    except:
      if self.date_taken is None:
        logging.warning(self.get_image_flename() + " - Filename datatime pattern unknown")
      return None

  def get_file_created(self):
    timestamp = os.path.getmtime(self.current_name)
    return datetime.fromtimestamp(timestamp, tz=None)

  def extract_file_created(self):
    full_text = self.get_file_created()
    return datetime.fromtimestamp(full_text, tz=None)

  def datetime_to_str(self, datatime):
    return datatime.strftime('%y-%m-%d_%H%M%S')

  def get_datetime_formatted(self):
    if self.date_taken is not None:
      return self.datetime_to_str(self.date_taken)
    elif self.date_filename is not None:
      return self.datetime_to_str(self.date_filename)
    else:
      return self.datetime_to_str(self.file_created)

  def __str__(self) -> str:
    return self.current_name + \
      "\n\t - Current Name: " + os.path.basename(self.current_name) + \
        "\n\t - Data Taken: " + str(self.date_taken) + \
          "\n\t - Data Filename: " + str(self.date_filename) + \
            "\n\t - File Created: " + str(self.file_created)
