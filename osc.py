from pythonosc import osc_message_builder
from pythonosc import udp_client

def simple_send():
    sender = udp_client.SimpleUDPClient('127.0.0.1', 4560)
    sender.send_message('/trigger/prophet', [70, 100, 8])

if __name__ == "__main__":
    simple_send()



