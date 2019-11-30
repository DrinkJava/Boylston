# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
import webrepl
from DHT import DHT
from AWSIOT import AWSMQTT
import json
import time

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active()
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(False)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('Juniper2.4', 'ginandtonic')
    print('network config:', sta_if.ifconfig())


do_connect()

dht = DHT()
client = AWSMQTT()
client.connect()
#webrepl.start()
x = 0
while(True):
    reading = dht.get_data()
    payload = json.dumps(reading)
    client.publish(payload)
    x += 1
    time.sleep(300)
gc.collect()

