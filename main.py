import pyautogui
import time

message = "Sorry Bondhu"  # Change this to your desired message
delay = 1  # Delay in seconds between messages

time.sleep(1)  # Wait 5 s
# econds before starting (for setup)

while True:
    pyautogui.typewrite(message)  # Type the message
    pyautogui.press("enter")  # Press Enter to send
    time.sleep(delay)  # Wait before sending the next message
