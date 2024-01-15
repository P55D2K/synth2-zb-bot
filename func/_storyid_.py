import os

def get_story_id():
  if not os.path.exists('data/story_id.txt'):
    with open('data/story_id.txt', 'w') as f:
      f.write('15')

  with open('data/story_id.txt', 'r') as f:
    story_id = f.read()

  if input("Would you like to change the story id? Your current story id is " + story_id + ". (y/n): ").lower().strip() == 'y':
    story_id = input("Please enter the new story id: ")
    update_story_id(story_id)
    print("Story ID saved.")

  return story_id

def update_story_id(current_story_id, increment=1):
  new_story_id = str(int(current_story_id) + increment)
  with open('data/story_id.txt', 'w') as f:
    f.write(new_story_id)
  return new_story_id