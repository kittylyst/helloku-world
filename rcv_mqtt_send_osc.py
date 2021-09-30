import os
import time
import uuid
import datetime
import json
from pprint import pprint
import paho.mqtt.client as mqtt
from pythonosc import osc_message_builder
from pythonosc import udp_client


def on_log(client, userdata, level, buf):
    print("log: ",buf)

def main_loop():
    sender = udp_client.SimpleUDPClient('127.0.0.1', 4560)

    def msg_rcv(client, userdata, message):
        # print("Received message '" + str(message.payload) + "' on topic '" + message.topic)
        try:
            data = json.loads(message.payload.decode('utf-8'))
            print(data["date"])
            sender.send_message('/trigger/prophet', [70, 100, 8])
        except:
            print("A message not intended for me, ignoring... "+ str(message.payload))

    client = mqtt.Client("bje_client_"+ str(uuid.UUID.hex))
    client.on_message = msg_rcv
    client.on_log = on_log
    client.connect("test.mosquitto.org") # , port=1883 , keepalive=60, bind_address=""
    client.loop_start()
    client.subscribe("test_for_anna")

    while True:
        time.sleep(0.1)
        #print(".")

if __name__ == "__main__":
    main_loop()