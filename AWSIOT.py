#AWS MQTT client cert example for esp8266 or esp32 running MicroPython 1.9 
from umqtt.robust import MQTTClient
import time

CERT_FILE = "/ssl/cert"
KEY_FILE = "/ssl/key"

#if you change the ClientId make sure update AWS policy
MQTT_CLIENT_ID = "esp8266"
MQTT_PORT = 8883

#if you change the topic make sure update AWS policy
MQTT_TOPIC = "iot/temperature"

#Change the following three settings to match your environment
MQTT_HOST = "a2aw05rnx9mbwo-ats.iot.us-west-2.amazonaws.com"

mqtt_client = None

class AWSMQTT:
    def __init__(self):
        self.client = None

    def connect(self):
        print("Attempting to connect to AWS IOT")
        try:
            with open(KEY_FILE, "r") as f: 
                key = f.read()
            print("Got Key")
            
            with open(CERT_FILE, "r") as f: 
                cert = f.read()
            print("Got Cert")	
            self.mqtt_client = MQTTClient(client_id=MQTT_CLIENT_ID, server=MQTT_HOST, port=MQTT_PORT, keepalive=5000, ssl=True, ssl_params={"cert":cert, "key":key, "server_side":False})
            self.mqtt_client.connect()
            print('MQTT Connected')
        except Exception as e:
            print('Cannot connect MQTT: ' + str(e))
            raise

    def publish(self, msg):
        try:    
            self.mqtt_client.publish(MQTT_TOPIC, msg)
            print("Sent: " + msg)
        except Exception as e:
            print("Exception publish: " + str(e))
            raise
