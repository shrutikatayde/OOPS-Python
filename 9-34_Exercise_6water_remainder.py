"""
Created on Sat Oct 29 15:59:57 2022
"""
# import os
import time
from plyer import notification

#
# command = (
#     "osascript -e 'say \"drink water\" ' ; osascript -e 'display alert \"drink water\"'"
# )

# os.system(command)

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Shrutika, Please drink water! ",
            message="Drink plenty of water every day and stay healthy",
            app_icon="",
            timeout=10,
        )
        time.sleep(60 * 60)
