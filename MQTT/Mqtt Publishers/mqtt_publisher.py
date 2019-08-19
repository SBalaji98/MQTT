import paho.mqtt.publish as publish

MQTT_SERVER = "192.168.0.172"
MQTT_PATH = "test_channel"

publish.single(MQTT_PATH, "hi this is a test message", hostname=MQTT_SERVER)