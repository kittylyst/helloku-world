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
        print("A message not intended for me, ignoring...")

def on_log(client, userdata, level, buf):
    print("log: ",buf)

def main_loop():
    # mosquitto_sub -h 82.165.16.151 -t UCC/mark
    client = mqtt.Client("bje_client_"+ str(uuid.UUID.hex))
    client.on_message = msg_rcv
    # client.on_log = on_log
    client.connect("82.165.16.151") # , port=1883 , keepalive=60, bind_address=""
    client.loop_start()
    client.subscribe("UCC/mark")

    while True:
        time.sleep(4)
        print(".")

if __name__ == "__main__":
    main_loop()