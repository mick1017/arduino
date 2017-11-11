import os
import glob
import time
import MySQLdb
 

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
db = MySQLdb.connect("localhost", "monitor", "password", "temps")
curs=db.cursor()




def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0

        return (  temp_f )
	
#while True:
#	print(read_temp())	
#	time.sleep(1)


#send_email( repr( read_temp() ) )

# note that I'm using triplle quotes for formatting purposes
# you can use one set of double quotes if you put the whole string on one line
dbString='INSERT INTO tempdat values(CURRENT_DATE(), NOW(), \'living room\',' + repr(read_temp())	 + ',0)'
print (dbString)
try:
    curs.execute (dbString)
    db.commit()
    print "Data committed"
except:
    print "Error: the database is being rolled back"
    db.rollback()



