import smtplib

smtpUser = 'xxx'
smtpPass = 'xxxx'

toAdd = 'mixx@kxxx.com' 
fromAdd = smtpUser

subject = ' Python Test'
header = 'To: ' + toAdd + '\n' + 'From: ' + fromAdd + '\n' + 'Subject: ' + subject
body = 'From within a Python Script'

print header + '\n' + body

s = smtplib.SMTP('smtp.gmail.com',587)

s.ehlo()
s.starttls()
s.ehlo()

s.login(smtpUser, smtpPass)
s.sendmail(fromAdd, toAdd, header + '\n' + body )

s.quit()


