from datetime import datetime
import paho.mqtt.publish as publish
import serial
import time

ser = serial.Serial('COM4')
ser.flushInput()
MQTT_SERVER = "192.168.0.172"
MQTT_PATH = ["test_channel", "OBD", "DOB"]

while True:

    ser_bytes = ser.readline().decode('utf-8')
    # pub1 = ser_splits[0]
    # pub2 = ser_splits[1]

    if ser_bytes.startswith("OBD"):
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        pub1 = ser_bytes.replace('OBD:','').split(",")
        payload = "{} {}".format('\n'.join(pub1),ts)
        publish.single(MQTT_PATH[1], payload, hostname=MQTT_SERVER)
        print(payload)
    elif ser_bytes.startswith("DOB"):
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        pub2 = ser_bytes.replace('DOB:','').split(",")
        payload = "{} {}".format('\n'.join(pub2),ts)
        publish.single(MQTT_PATH[2], payload, hostname=MQTT_SERVER)
        print(payload)