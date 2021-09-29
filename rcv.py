import os
import time
import uuid
import datetime
import json
from pprint import pprint
import paho.mqtt.client as mqtt

def msg_rcv(client, userdata, message):
    # print("Received message '" + str(message.payload) + "' on topic '" + message.topic)
    try:
        data = json.loads(str(message.payload))
        print(data["date"])
    except:
        print("A message not intended for me, ignoring... "+ str(message.payload))

def on_log(client, userdata, level, buf):
    print("log: ",buf)

def main_loop():
    # mosquitto_sub -h 82.165.16.151 -t UCC/mark
    client = mqtt.Client("bje_client_"+ str(uuid.UUID.hex))
    client.on_message = msg_rcv
    # client.on_log = on_log
    client.connect("test.mosquitto.org") # , port=1883 , keepalive=60, bind_address=""
    client.loop_start()
    client.subscribe("test_for_anna")

    while True:
        time.sleep(1)
        print(".")

if __name__ == "__main__":
    main_loop()