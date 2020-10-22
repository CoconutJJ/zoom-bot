# zoom-bot
A Zoom bot that joins meeting for you

Use cron jobs to start script at scheduled time.

Make sure to fill in the `record()` function or your lecture won't be recorded!

Currently targets only technical users, however if someone can make this also for non-technical people that would be great.

Suggested Recording Software: https://obsproject.com/

## Install Dependencies
```
pip install pyautogui
```
## Run
Run in the directory with icons/ folder.
```
python zoom_auto.py MEETING_ID MEETING_PASSWORD
```