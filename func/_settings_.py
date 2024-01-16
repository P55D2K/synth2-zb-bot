import os
import json

def get_dev_mode():
  if input("Would you like to run the program in developer mode? (y/n): ").lower().strip() == 'y':
    print("Developer mode enabled.\n")
    return True
  return False

def load_data():
  if os.path.exists('settings.json'):
    with open('settings.json') as f:
      if os.stat('settings.json').st_size == 0:
        return False

      data = json.load(f)
      skip_intro = data.get('skip_intro')

      if skip_intro == None:
        skip_intro = False
    
      return skip_intro
    
  return False