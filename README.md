# zoom-bot
A Zoom bot that joins meeting for you

Use cron jobs to start script at scheduled time.

Been updated to support built-in screen and audio recording. Currently
only been tested on Linux devices.

## Install Dependencies
```
pip install -r requirements.txt
```
## Run
```
python zoom_auto.py [Zoom Meeting Id] [Zoom Meeting Password] [Duration in Minutes] [Out File]
```