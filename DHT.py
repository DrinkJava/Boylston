from dht import DHT11
import machine

class DHT:
    def __init__(self):
        self.sensor = DHT11(machine.Pin(5))
        
    def get_data(self):
        self.sensor.measure()
        temp = self.sensor.temperature()
        hum = self.sensor.humidity()
        return {"temperature": temp, "humidity": hum}
