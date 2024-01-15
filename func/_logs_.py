import os

def update_log(new_log):
  if not os.path.exists('data/log.txt'):
    with open('data/log.txt', 'w') as f:
      pass

  with open('data/log.txt', 'a') as log:
    log.write(new_log + '\n')