import imaplib
import email
from email.header import decode_header
import os
import time
class MailChecker:
    def __init__(self, mail_address, mail_password, imap_server, mail_list):
        self.mail_address = mail_address
        self.mail_password = mail_password
        self.imap_server = imap_server
        self.mail_list = mail_list
        self.imap = imaplib.IMAP4_SSL(self.imap_server)
        self.imap.login(self.mail_address, self.mail_password)
        self.checked_mails = set()
    def verify_mail(self, from_mail: str):
        for module, mails in self.mail_list.items():
            for mail in mails:
                if mail in from_mail:
                    return True, module
        return False, "No Module"
    def check_mail(self):
        status, messages = self.imap.select("INBOX")
        N = 3
        messages = int(messages[0])
        print(messages)
        for i in range(messages, messages-N, -1):
            if i not in self.checked_mails:
                res, msg = self.imap.fetch(str(i), "(RFC822)")
                for response in msg:
                    if isinstance(response, tuple):
                        msg = email.message_from_bytes(response[1])
                        subject = MailChecker.decode_header(msg["Subject"])
                        From = MailChecker.decode_header(msg.get("From"))
                        if msg.is_multipart() and self.verify_mail(From)[0]:
                            for part in msg.walk():
                                content_disposition = str(
                                    part.get("Content-Disposition"))
                                if "attachment" in content_disposition:
                                    filename = part.get_filename()
                                    if filename:
                                        folder_name = f"output/{self.verify_mail(From)[1]}"
                                        if not os.path.isdir(folder_name):
                                            os.mkdir(folder_name)
                                        open(f"{folder_name}/{filename}", "wb").write(
                                            part.get_payload(decode=True))
                self.checked_mails.add(i)
    @staticmethod
    def decode_header(header):
        decoded_header, encoding = decode_header(header)[0]
        if isinstance(decoded_header, bytes):
            decoded_header = decoded_header.decode(encoding)
        return decoded_header
if __name__ == "__main__":
    MAIL_ADRESS = 'YOUR_MAIL_ADRESS'
    MAIL_PASSWORD = 'YOUR_MAIL_PASSWORD'
    mail_list = {
        "meca": ["mecaniqueproffesor1@gmail.com"]}
    mail_checker = MailChecker(
        MAIL_ADRESS, MAIL_PASSWORD, "imap.gmail.com", mail_list)
    while True:
        mail_checker.check_mail()
        time.sleep(120)
