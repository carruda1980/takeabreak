import time
import webbrowser

break_count = 0
while(break_count < 9):
    # Putting the script to wait 10 seconds
    time.sleep(30 * 60)
    # oppening a youtube video motivation
    webbrowser.open("https://www.youtube.com/watch?v=pEa5N1hwy6s")
    break_count = break_count + 1
else:
    print("Now it`s time to go home!")