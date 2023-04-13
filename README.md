# Email Attachment Downloader

This is a Python script that uses the `imaplib` and `email` modules to download email attachments from a specified email account.

## Requirements

- Python 3.x
- `imaplib`
- `email`

## Setup

1. Install the required modules .
2. Open the script in a text editor and set the `MAIL_ADDRESS`, `MAIL_PASSWORD`, and `imap_server` variables to the appropriate values for your email account.
3. Set the `mailList` variable to a dictionary where the keys are folder names and the values are lists of email addresses. Emails from addresses in these lists will have their attachments downloaded to the corresponding folder.

## Usage

1. Run the script by navigating to its directory in your terminal and running `python <script_name>.py`.
2. The script will download attachments from emails in the specified email account and save them to folders named after the keys in the `mailList` dictionary.

## Notes

- The script currently only checks the most recent 3 emails in the inbox. You can change this by modifying the value of the `N` variable in the `check_mail` function.
- The script only downloads attachments from emails sent by addresses specified in the `mailList` dictionary.
