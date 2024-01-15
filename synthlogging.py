import time
from func._logs_ import *
from func._general_ import *
from synthconstants import *

def start_session():
  update_log("\n--- SESSION STARTED ---")
  update_log("DateTime: " + time.strftime("%H:%M:%S", time.localtime()) + ", " + time.strftime("%d/%m/%Y", time.localtime()) + "\n")

  print(big_text)
  print("Copyright 2023. All rights reserved. (c) ZK\n")

  return time.time()

def instructions():
  print("\nTo exit, press Ctrl + C")
  time.sleep(1)
  print("You can continue doing other things while this program is running")
  time.sleep(1)
  print("Do not close the browser window that opens, or login to ZBSchools from somewhere else.")
  time.sleep(1)
  print("If there is an error, increase the story ID by 1 and try again.")
  time.sleep(1)

def end_session(session_start_time, quizzes_per_min, points_per_min, quizzes_completed_this_session):
  update_log(f"\nSession Duration: {convert_seconds(round(time.time() - session_start_time))}")
  update_log(f"Average Quizzes Per Minute: {round(sum(quizzes_per_min) / len(quizzes_per_min), 2)}")
  update_log(f"Average Points Per Minute: {round(sum(points_per_min) / len(points_per_min), 2)}")
  update_log(f"Total Quizzes Completed: {quizzes_completed_this_session}")
  update_log(f"Total Points Gained: {quizzes_completed_this_session * 150}")
  update_log("--- SESSION ENDED ---\n")

  print("\033c--- SESSION ENDED ---"); time.sleep(1)
  print(f"Session Duration: {convert_seconds(round(time.time() - session_start_time))}"); time.sleep(1)
  print(f"Average Quizzes Per Minute: {round(sum(quizzes_per_min) / len(quizzes_per_min), 2)}"); time.sleep(1)
  print(f"Average Points Per Minute: {round(sum(points_per_min) / len(points_per_min), 2)}"); time.sleep(1)
  print(f"Total Quizzes Completed: {quizzes_completed_this_session}")
  print(f"Total Points Gained: {quizzes_completed_this_session * 150}")


