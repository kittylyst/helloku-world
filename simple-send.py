import os
import datetime
import json
import paho.mqtt.client as mqtt

def current_date():
    rightnow = str(datetime.datetime.now())
    # mosquitto_pub -h 82.165.16.151 -m "Hi" -t UCC/mark
    client = mqtt.Client("bje_client_test1")
    client.connect("test.mosquitto.org") # , port=1883 , keepalive=60, bind_address=""
    client.publish("test_for_anna", json.dumps({"date": rightnow}))
	
if __name__ == "__main__":
    current_date()
