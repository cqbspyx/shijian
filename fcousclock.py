# shijian
import time

def focus_timer(minutes):
    seconds = minutes * 60
    start_time = time.time()
    end_time = start_time + seconds

    while time.time() < end_time:
        remaining_seconds = int(end_time - time.time())
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        timer_display = f"{minutes:02d}:{seconds:02d}"
        print(f"Time remaining: {timer_display}", end="\r")
        time.sleep(1)

    print("\nTime's up! Stay focused!")
