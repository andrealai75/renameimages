from datetime import datetime

class StringDate:
  def __init__(self, year, month, day, hour, minute, seconds):
    self.year = year
    self.month = month
    self.day = day
    self.hour = hour
    self.minute = minute
    self.seconds = seconds

  def is_a_year(self):
    if self.year.isnumeric() and \
      00 <= int(self.year) <= 99:
      return True
    else:
      return False

  def is_a_month(self):
    if self.month.isnumeric() and \
      1 <= int(self.month) <= 12:
      return True
    else:
      return False

  def is_a_day(self):
    if self.day.isnumeric() and \
      1 <= int(self.day) <= 31:
      return True
    else:
      return False

  def is_a_hour(self):
    if self.year.isnumeric() and \
      0 <= int(self.year) <= 59:
      return True
    else:
      return False

  def is_a_minute(self):
    if self.minute.isnumeric() and \
      0 <= int(self.minute) <= 59:
      return True
    else:
      return False

  def is_a_seconds(self):
    if self.seconds.isnumeric() and \
      0 <= int(self.seconds) <= 59:
      return True
    else:
      return False


  def is_a_date(self):
    valid = True
    valid = valid and self.is_a_year()
    valid = valid and self.is_a_month()
    valid = valid and self.is_a_day()
    valid = valid and self.is_a_hour()
    valid = valid and self.is_a_minute()
    valid = valid and self.is_a_seconds()
    return valid

  def __str__(self) -> str:
      return \
        self.year + "-" + \
        self.month + "-" + \
        self.day + "_" + \
        self.hour + \
        self.minute + \
        self.seconds