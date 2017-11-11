


def sendMail(FROM,TO,SUBJECT,TEXT,SERVER):
    import smtplib
    """this is some test documentation in the function"""
    message = """\
    From: %s
    To: %s
    Subject: %s
    %s  """ % (FROM, ", ".join(TO), SUBJECT, TEXT)


    # Configure the SMTP_SSL protocol and communicate with the server
   # server = smtplib.SMTP_SSL(SERVER, 465)
#    server.set_debuglevel(1)
    #server.ehlo

    server = smtplib.SMTP(SERVER)
    server.sendmail(FROM, TO, message)
    server.quit()

    # Send user authentication information
    #server.login('mickey@kmcalcara.com', 'molly123')   

    # Send the mail
    #server = smtplib.SMTP(SERVER)
#    server.sendmail(FROM, TO, message )
    print ('sending message ')
  #  server.quit()
    print ('quit')





SERVER = 'smtp.gmail.com'

sendMail('xxx','xxx', 'test','tst', SERVER)
