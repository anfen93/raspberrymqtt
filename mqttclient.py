import paho.mqtt.client as mqtt
import pifacedigitalio as p

MQTT_SERVER="192.168.120.10"
MQTT_PATH1="CMD/POWER1"
MQTT_PATH2="CMD/POWER2"

p.init()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(MQTT_PATH1)
    client.subscribe(MQTT_PATH2)

def on_message(client, userdata, msg):
    value=0

    if ("OFF" in str(msg.payload)):
        value=0
        valuestr="OFF"

    if ("ON" in str(msg.payload)):
        value=1
        valuestr="ON"

    if (msg.topic=="CMD/POWER1"):
        p.digital_write(0,value)
        print("Assigned value {} to topic CMD/POWER1".format(valuestr))

    if (msg.topic=="CMD/POWER2"):
        p.digital_write(1,value)
        print("Assigned value {} to topic CMD/POWER2".format(valuestr))


p.init()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_SERVER, 1883, 60)

client.loop_forever()
