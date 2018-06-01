# Raspberry MQTT client


Simple Python Script for communicating from a raspberry to a MQTT Broker

# Installation and configuration



## Requirements

* Raspberry pi with PiFace and Python 3
* A Mosquitto Broker Server
* mosquitto_pub for testing
* pip3
* paho.mqtt.client
* pifacedigitalio


## Installation:
* Install pip3 and pifacedigitalio
    ```
    $ sudo apt install python3-pip
    $ sudo pip3 install paho-mqtt
    $ sudo apt install python{,3}-pifacedigitalio
    ```
* Copy mqttclient.py and mqttclient.service on /home/pi/

* Copy mqttclient.service to /lib/systemd/system
    ```
   $ sudo cp mqttclient.service /lib/systemd/system
    ```
* Give read only permission to mqttclient.service
    ```
   $ sudo chmod 644 /lib/systemd/system/mqttclient.service
    ```
* Give execution permission to mqttclient.py
    ```
   $ chmod+x /home/pi/mqttclient.py
    ```
* Reload systemctl
    ```
   $ systemctl daemon-reload
    ```
* Enable and start service
    ```
   $ sudo systemctl enable mqttclient.service
   $ sudo systemctl start mqttclient.service
    ```
* Check service status
    ```
   $ sudo systemctl status mqttclient.service
    ```
* in a second terminal, run:
    ```
    mosquitto_sub -h yourip -t CMD/POWER1 -m "ON"
    ```
* In a third terminal, run:
     ```
    mosquitto_pub -h yourip -t CMD/POWER1 -m "ON"
     ```
* If everything is ok, you should read
    ```
    POWER1 ON
    ```
