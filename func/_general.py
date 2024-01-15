def remove(string, removestr):
  return string.replace(removestr, "")

def convert_seconds(seconds):
  seconds = seconds % (24 * 3600)
  hour = seconds // 3600
  seconds %= 3600
  minutes = seconds // 60
  seconds %= 60
     
  return (str(hour) + "hr " + str(minutes) + "min " + str(seconds) + "s")