from smtplib import SMTP
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

class mail:
    def __init__(self, host, port):
        self.smtp = SMTP(host, port)
        self.smtp.ehlo()
        self.smtp.starttls()
        self.smtp.ehlo()

    def connect(self, login, passwd):
        self.from_addr = login
        self.smtp.login(login, passwd)
    
    def send_message(self, addr, subj, message, file):

        msg = MIMEMultipart()
        msg['From'] = self.from_addr
        msg['To'] = COMMASPACE.join(addr)
        msg['Subject'] = subj

        msg.attach(MIMEText(message))

        with open(file, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(file)
            )
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(file)
        msg.attach(part)

        self.smtp.sendmail(self.from_addr, [addr], msg.as_string())

    def disconnect(self):
        self.smtp.quit()
