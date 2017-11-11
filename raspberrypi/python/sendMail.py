
import MySQLdb
from datetime import datetime
import traceback
import sys
import time
	
tempDataStr=''

def send_email(BODY):
	import smtplib

	smtpUser = 'xxxx'
	smtpPass = 'xxx'

	toAdd = ["addemal", "addemail"] 
	
	fromAdd = smtpUser
	toAddHdrStr = ", ".join(toAdd)

	subject = 'Living room Temperature Report' 
	header = 'To: ' + toAddHdrStr + '\n' + 'From: ' + fromAdd + '\n' + 'Subject: ' + subject
	body =  BODY

	#print header + '\n' + body

	s = smtplib.SMTP('smtp.gmail.com',587)

	s.ehlo()
	s.starttls()
	s.ehlo()

	s.login(smtpUser, smtpPass)
	s.sendmail(fromAdd, toAdd, header + '\n\n' + body )

	s.quit()



db = MySQLdb.connect("localhost", "monitor", "password", "temps")
curs=db.cursor()

dbDetailString='select tdate, ttime, temperature from tempdat where tdate=CURRENT_DATE()'
dbTodayAvgTempSQLStr='select avg(temperature) from tempdat where tdate=current_date()'
dbYesterdayAvgTempSQLStr='select avg(temperature) from tempdat where tdate=current_date()-1'
#print (dbDetailString)

targetTimepattern = '%I:%M %p'
originalTimeStr = ''
newTimeStr = ''
tempBodyStr = '\n\n##################################################################################\n\n'
tempDetailDataStr =''
todayAvgTemp = ''
yesterdayAvgTemp = ''

try:
    curs.execute (dbDetailString)
    fields = curs.fetchall()				
   

    for field in fields:
	#value = datetime.timedelta(0, row[0])
	#value = (datetime.datetime.min + value).time()
	originalTimeStr	=  datetime.strptime(str(field[1]), "%H:%M:%S")  
	newTimeStr = originalTimeStr.strftime(targetTimepattern)	
	tempDetailDataStr = tempDetailDataStr + '\n' + str(field[0]) + '  ' +  newTimeStr +  '  ' + str(field[2])	
       
    curs.execute (dbTodayAvgTempSQLStr)
    fields = curs.fetchall()
    todayAvgTemp=str(fields[0][0])
    #print('avgtemp: ' + todayAvgTemp )

    curs.execute (dbYesterdayAvgTempSQLStr)
    fields = curs.fetchall()
    yesterdayAvgTemp=str(fields[0][0])
    #print('yesterdayAvgTemp: ' + yesterdayAvgTemp)

except:
    print "Error: the database"
    traceback.print_exc(file=sys.stdout)
  #  db.rollback()
tempBodyStr = tempBodyStr + '\nAs of:' + str(datetime.now() )+ '\n\n'
tempBodyStr = tempBodyStr + '\nToday\'s Average Temperature: ' + todayAvgTemp + '\n'
tempBodyStr = tempBodyStr + '\nYesterday\'s Average Temperature: ' + yesterdayAvgTemp + '\n'
tempBodyStr = tempBodyStr + '\nToday\'s Detailed Temperatures:' + '\n' + tempDetailDataStr
send_email(tempBodyStr)

