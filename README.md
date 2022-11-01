# UltiLoggerV2

This is second version of previous UltiLogger repo: https://github.com/Kammelleon/UltiLogger

# Preparation

This app was tested only on Windows 10.
In order to use this you should have a Gmail account and 2FA enabled on it.
Next, you need to generate app password (as Google disabled less secure apps).
You can do it here: https://myaccount.google.com/apppasswords After that you can provide
your app password inside main.py:

```python
gmail = Gmail(app_password=YOUR_APP_PASSWORD,...
```
And define your Gmail sender address connected with generated app password:
```python
gmail.sender_address = SENDER_ADDRESS_CONNECTED_WITH_APP_PASSWORD
```
Now you are ready to the next step

# Usage

After preparation stage you can now set some settings according to your requirements
such as time to send email, time to log datetime inside log file etc.
In order to do this you can set the following variables:
- log_file_location - defines the location where logs will be saved
- screen_recorder_file_location - defines the location where screen recording file will be saved
- datetime_log_timeout - defines the time after which the datetime will be logged into log file
```python
log_handler = LogHandler(... datetime_log_timeout=10)
```
- video_length - defines the time after which logs with screen recorder will be sent to receiver address. It also defines the video length of the screen recorder
```python
screen_recorder = ScreenRecorder(video_length=5,...)
```

Then you can run the program with the following command:
```bash
python3 -m "ultiloggerv2"
```