## Recording video/audio from video conferencing calls
If you’re looking to use this repo to retrieve video or audio streams from meeting platforms like Zoom, Google Meet, Microsoft Teams, consider checking out [Recall.ai](https://www.recall.ai), an API for meeting recording.

# zoom-bot
A Zoom bot that joins meeting for you

Use cron jobs to start script at scheduled time.

Been updated to support built-in screen and audio recording. Currently
only been tested on Linux devices.


## Update: May 27th 2021 

This little script seems to have attracted a bit of attention, I've updated the
dependencies and documented a few issues to make this more up to date.

- `pip` may have difficulties installing `pyaudio` if the `portaudio.h` headers
  and respective library is missing from your computer. I got around this by
  installing `python-pyaudio` through my OS package manager. To that end this
  post on StackOverflow:
  https://stackoverflow.com/questions/5921947/pyaudio-installation-error-command-gcc-failed-with-exit-status-1
  seems provides many other solutions including the one I mentioned above.

- Currently, the script also records external mic input which was not what I had
  desired when I first wrote this little bot. I could never figure out how to
  only record system sound and ignore the mic. If your intents align with the fix
  of this issue, any ideas or actual changes would be much appreciated!


## Install Dependencies
```
pip install -r requirements.txt
```
## Run
```
python zoom_auto.py [Zoom Meeting Id] [Zoom Meeting Password] [Duration in Minutes] [Out File]
```
