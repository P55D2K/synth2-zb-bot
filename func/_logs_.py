import os

def update_log(new_log):
  if not os.path.exists('data/log.txt'):
    with open('data/log.txt', 'w') as f:
      pass

  with open('data/log.txt', 'a') as log:
    log.write(new_log + '\n')

def update_answers(story_number, answers):
  if not os.path.exists('data/answers.txt'):
    with open('data/answers.txt', 'w') as f:
      pass

  with open('data/answers.txt', 'r') as f:
    lines = f.readlines()

  for i in range(len(lines)):
    if lines[i].split(' | ')[0] == str(story_number):
      lines[i] = str(story_number) + ' | ' + ', '.join([str(answer) for answer in answers]) + '\n'
      break
  else:
    lines.append(str(story_number) + ' | ' + ', '.join([str(answer) for answer in answers]) + '\n')

  with open('data/answers.txt', 'w') as f:
    f.writelines(lines)