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

    # Counter state
    clicks = {"RED": 0, "YELLOW": 0, "GREEN": 0, "BLUE": 0}
    #
    # Static maps of the modulo values each button has
    #
    red_values = [1, 2, 3, 4, 5]
    green_values = [0.1, 0.25]
    yellow_values = [5, 10, 20, 10, 5]
    blue_values = [80, 40]

    mapped_values = {"RED": red_values, "YELLOW": yellow_values, "GREEN": green_values, "BLUE": blue_values}

    def msg_rcv(client, userdata, message):
        # print("Received message '" + str(message.payload) + "' on topic '" + message.topic)
        try:
            data = json.loads(message.payload.decode('utf-8'))
            print(data["date"])
            val = data["value"]
            clicks[val] = clicks[val] + 1
            to_send = [red_values[clicks["RED"] % len(red_values)], yellow_values[clicks["YELLOW"] % len(yellow_values)], green_values[clicks["GREEN"] % len(green_values)], blue_values[clicks["BLUE"] %len(blue_values)] ]
            print(clicks)
            print(to_send)

            sender.send_message('/trigger/prophet', to_send)
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