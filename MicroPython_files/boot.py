# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import gc
import webrepl
import network
webrepl.start()
gc.collect()

sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)

def do_conn():
	if not sta_if.isconnected():
		print("Connecting to network ......")
		sta_if.active(True)
		sta_if.connect('CL24Ghz', 'CL2016Sec')
		while not sta_if.isconnected():
			pass
	print("Network Config :", sta_if.ifconfig())


do_conn()

