
import time
import RPi.GPIO as io
io.setmode(io.BCM)

pir_pin = 18

io.setup(pir_pin, io.IN)
io.setup(27,io.OUT)
io.setup(22,io.OUT)

io.output(22,io.LOW)
io.output(27,io.LOW)
try:
	while True:
		if io.input(pir_pin):
			print("Pir detects movement")
			io.output(22,io.HIGH)
			io.output(27,io.HIGH)
			time.sleep(.5)
		io.output(22,io.LOW)
		io.output(27,io.LOW)
except KeyboardInterrupt:
	pass
finally:
	io.cleanup()


	

	
	


