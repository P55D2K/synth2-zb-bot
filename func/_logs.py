def update_log(new_log):
  with open('data/log.txt', 'a') as log:
    log.write(new_log + '\n')