# TeamsJoiner

This is a Microsoft Teams bot that automatically attends meetings with no human interaction besides the 2FA notification.

The bot executes as follow:
1. Opens Google Chrome
2. Goes to MS Teams
3. Logs in with the user's credentials
4. Opens the meeting link set by the user
5. Turns off the microphone
6. Joins the meeting

## Prerequesites

- Google Chrome
- Microsoft account
- 2FA enabled with Microsoft Authenticator

## Configuration
- `pip install -r requirements.txt`
- Add meeting link to **meetinglinks.py** as a variable
- In **Bot.py** main function, change `bot.join_meeting(class_1)` to `bot.join_meeting(<your variable here>)`
- Add your MS Teams credentials to **LoginCredentials.py**

### Optional
Set up a task scheduler to automatically execute **Bot.py** according to your class schedule. On Linux, you can use something like cron jobs. On Windows, you can use the built in task scheduler.

**NOTE:** this script handles login credentials in plaintext. It might be a good idea to edit the permissions on **LoginCredentials.py** to prevent unwanted eyes.

## TODO:
- Properly encrypt user credentials.
- Add discord webhooks to update the user on script execution.
- Add logic to handle different scenarios.
- Add command line arguments to determine which link should be opened.
