import socket
import machine
import time


#HTML to send to browser
html = """<!DOCTYPE html>
<html>
<head>
<title> TRIAL </title>
<style>
body {background-color: yeallow}
h1 {color:red}

button {
	color: red;
	height: 200px;
	width: 150px;
	background: blue;
	border: 3px solid #4CAF50; /* Green */
	border-radius: 50%;
	font-sizeL 250%;
	position: center;
}
</style>
</head>
<body>
<center> <h1> Light Trial </h1>
<form>
<div> <button name="CMD" value="on" type="submit"> ON </button> </div>
<div> <button name="CMD" value="off" type="submit"> OFF </button> </div>
</form>
</center>
</body>
</html>
"""

p2 = machine.Pin(2, machine.Pin.OUT)

def Ton():
	p2.on()

def Toff():
	p2.off()

#setup socket webserver
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket()

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(('', 80))
s.listen(5)

print("Listening, connect your browser to http://<this_host>:80/")

counter = 0

while True:
	conn, addr = s.accept()
	print("Get connection from %s" % str(addr))
	request = conn.recv(1024)
	print("Content = %s" % str(request))
	request = str(request)

	CMD_on = request.find('/?CMD=on')
	CMD_off = request.find('/?CMD=off')

	if CMD_on == 6:
		print("+LEDon")
		Ton()

	if CMD_off == 6:
		print("+LEDoff")
		Toff()

	response = html
	conn.send(response)
	conn.close()

