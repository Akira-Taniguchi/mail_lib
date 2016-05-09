# -*- coding: utf-8 -*-
import os
import smtplib
import mimetypes
from email import Encoders
from email.mime.text import MIMEText
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart
from email.Utils import formatdate
from email.Utils import formataddr


def send_mail(to_addr_list, subject, message, from_addr, smtp_host, smtp_port=25, cc_addr_list=[], bcc_addr_list=[]):
    msg = MIMEText(message, _charset='utf-8')
    msg.set_unixfrom('author')
    if len(to_addr_list) != 0:
        msg['To'] = ','.join(to_addr_list)
    if len(cc_addr_list) != 0:
        msg['Cc'] = ','.join(cc_addr_list)
    if len(bcc_addr_list) != 0:
        msg['Bcc'] = ','.join(bcc_addr_list)
    msg['From'] = formataddr(('Author', from_addr))
    msg['Subject'] = subject
    msg['Date'] = formatdate(localtime=True)
    s = smtplib.SMTP(smtp_host, smtp_port)
    s.sendmail(from_addr,
               to_addr_list, msg.as_string())
    s.quit()


def send_attach_file_mail(to_addr_list, subject, message, file_path, from_addr, smtp_host, smtp_port=25,
                          cc_addr_list=[], bcc_addr_list=[]):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = formataddr(('Author', from_addr))
    if len(to_addr_list) != 0:
        msg['To'] = ','.join(to_addr_list)
    if len(cc_addr_list) != 0:
        msg['Cc'] = ','.join(cc_addr_list)
    if len(bcc_addr_list) != 0:
        msg['Bcc'] = ','.join(bcc_addr_list)
    msg['Date'] = formatdate(localtime=True)
    message = MIMEText(message, _charset='utf-8')
    msg.attach(message)
    mime_type, sub_type = mimetypes.guess_type(file_path)
    attachment = MIMEBase(mime_type, sub_type)
    with open(file_path) as attach_file_obj:
        attachment.set_payload(attach_file_obj.read())
    Encoders.encode_base64(attachment)
    msg.attach(attachment)
    attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file_path))
    s = smtplib.SMTP(smtp_host, smtp_port)
    s.sendmail(from_addr,
               to_addr_list, msg.as_string())
    s.quit()
