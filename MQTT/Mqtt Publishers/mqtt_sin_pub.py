from datetime import datetime
import paho.mqtt.publish as publish
import serial
import time

ser = serial.Serial('COM4')
ser.flushInput()
MQTT_SERVER = "192.168.0.172"
MQTT_PATH = "test_channel"

while True:
    try:
        ser_bytes = ser.readline().decode('utf-8')
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        payload = "{} {}".format(ts,ser_bytes)
        publish.single(MQTT_PATH, payload , hostname=MQTT_SERVER)
        print(payload)
        time.sleep(5)
    except:
        print("Keyboard Interrupt")
        break

