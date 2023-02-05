# TeamsJoiner

This is a Microsoft Teams bot that automatically attends meetings with no human interaction besides the 2FA notification.

## Prerequesites

- Google Chrome
- Microsoft account
- 2FA Enabled through Microsoft Authenticator

## Configuration

- Add meeting link to **meetinglinks.py** as a variable
- In **Bot.py** main function, change `bot.join_meeting(class_1)` to `bot.join_meeting(<your variable here>)`
