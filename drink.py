import time
import chime

chime.theme("sonic")

DRINK_INTERVAL = 2400  # seconds (40 minutes)
drink_count = 0

while True:
    try:
        print("DRINK!!!")
        drink_count += 1
        chime.warning()
        time.sleep(DRINK_INTERVAL)

    except KeyboardInterrupt:
        print(f"Ok fine, I'll stop. You drank {drink_count} times... roughly.")
        break