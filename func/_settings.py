def get_dev_mode():
  if input("Would you like to run the program in developer mode? (y/n): ").lower().strip() == 'y':
    print("Developer mode enabled.\n")
    return True
  return False