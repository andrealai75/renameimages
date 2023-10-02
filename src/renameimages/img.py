import os, sys
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime

from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from renameimages.string_date import StringDate

class Img:
  def __init__(self, current_name):
    self.current_name = current_name
    self.date_taken = ""
    self.date_filename = ""
    self.file_created = ""
    self.datetime_formatted = ""

  def get_file_name(self):
    return os.path.basename(self.current_name)

  def get_datetime_formatted(self):
    return self.datetime_formatted

  def get_date_taken(self):
    image = Image.open(self.current_name)
    exifdata = image.getexif()
    for tag_id in exifdata:
      tag = TAGS.get(tag_id, tag_id)
      if tag == "DateTime":
        return exifdata.get(tag_id)

  def extract_data_taken(self):
    full_text = self.get_date_taken()
    if full_text:
      date = StringDate( \
        full_text[2:4], full_text[5:7], full_text[8:10], \
          full_text[11:13], full_text[14:16], full_text[17:19])
      if date.is_a_date():
        self.date_taken = str(date)

  def extract_data_filename(self):
    file = os.path.basename(self.current_name)
    date = StringDate( \
      file[2:4], file[4:6], file[6:8], \
        file[9:11], file[11:13], file[13:15])
    if date.is_a_date():
      self.date_filename = str(date)

  def get_file_created(self):
    timestamp = os.path.getmtime(self.current_name)
    file_created = datetime.fromtimestamp(timestamp, tz=None)
    return str(file_created)

  def extract_file_created(self):
    full_text = self.get_file_created()
    if full_text:
      date = StringDate( \
        full_text[2:4], full_text[5:7], full_text[8:10], \
          full_text[11:13], full_text[14:16], full_text[17:19])
      if date.is_a_date():
        self.file_created = str(date)
  
  def set_datetime_formatted(self):
    if self.date_taken:
      self.datetime_formatted = self.date_taken
    elif self.date_filename:
      self.datetime_formatted = self.date_filename
    else:
      self.datetime_formatted = self.file_created

  def extract_info(self):
    self.extract_data_taken()
    self.extract_data_filename()
    self.extract_file_created()
    self.set_datetime_formatted()

  def __str__(self) -> str:
      return self.current_name + \
          "\n\t - Data Taken: " + self.date_taken + \
            "\n\t - Data Filename: " + self.date_filename + \
              "\n\t - File Created: " + self.file_created  + \
                "\n\t - File Created: " + self.datetime_formatted
