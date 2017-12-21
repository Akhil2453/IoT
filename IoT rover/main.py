import socket
import machine
import time 


#HTML to send to browsers
html = """<!DOCTYPE html>
<html>
<head>
<title>Botdemy MicroPython IoT Car</title>
<style>
body {background-color: black}
h1 {color:red}

button {
        color: red;
        height: 200px;
        width: 200px;
        background:black;
        border: 3px solid #4CAF50; /* Green */
        border-radius: 50%;
        font-size: 250%;
        position: center;
}
</style>
</head>
<body>
<center><h1>Botdemy IoT Car Control</h1>
<form>
<div><button name="CMD" value="forward" type="submit">Forward</button></div>
<div><button name="CMD" value="left" type="submit">Left</button>
<button name="CMD" value="stop" type="submit">Stop</button>
<button name="CMD" value="right" type="submit">Right</button></div>
<div><button name="CMD" value="back" type="submit">Back</button></div>
</form>
</center>
</body>
</html>
"""


#Wemos Dpin to GPIO
#https://www.wemos.cc/product/d1.html
#D1->GPIO5
#D2->GIOO4
#D3->GPIO0
#skip D4 - built-in LED)
#D5->GPI014
Lmotor1 = machine.Pin(5, machine.Pin.OUT)
Lmotor2 = machine.Pin(4, machine.Pin.OUT)

Rmotor1 = machine.Pin(0, machine.Pin.OUT)
Rmotor2 = machine.Pin(14, machine.Pin.OUT)


def forward():
  Lmotor1.high()
  Lmotor2.low()
  Rmotor1.high()
  Rmotor2.low()

def back():
  Lmotor1.low()
  Lmotor2.high()
  Rmotor1.low()
  Rmotor2.high()

def left():
  Lmotor1.low()
  Lmotor2.high()
  Rmotor1.high()
  Rmotor2.low()
  time.sleep_ms(100)
  stop()

def right():
  Lmotor1.high()
  Lmotor2.low()
  Rmotor1.low()
  Rmotor2.high()
  time.sleep_ms(100)
  stop()

def stop():
  Lmotor1.low()
  Lmotor2.low()
  Rmotor1.low()
  Rmotor2.low()
 
#Setup Socket WebServer
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket()

#new?
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(('', 80))
s.listen(5)
print("Listening, connect your browser to http://<this_host>:80/")

counter = 0

while True:
    conn, addr = s.accept()
    print("Got a connection from %s" % str(addr))
    request = conn.recv(1024)
    print("Content = %s" % str(request))
    request = str(request)

    CMD_forward = request.find('/?CMD=forward')
    CMD_back = request.find('/?CMD=back')
    CMD_left = request.find('/?CMD=left')
    CMD_right = request.find('/?CMD=right')
    CMD_stop = request.find('/?CMD=stop')

    #print("Data: " + str(CMD_forward))
    #print("Data: " + str(CMD_back))
    #print("Data: " + str(CMD_left))
    #print("Data: " + str(CMD_right))
    #print("Data: " + str(CMD_stop))

    if CMD_forward == 6:
        print('+forward')
        forward()
    if CMD_back == 6:
        print('+back')
        back()
    if CMD_left == 6:
        print('+left')
        left()
    if CMD_right == 6:
        print('+right')
        right()
    if CMD_stop == 6:
        print('+stop')
        stop()
    response = html
    conn.send(response)
    conn.close()
