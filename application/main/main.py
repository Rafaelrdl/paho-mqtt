import time
from application.configs.broker_configs import mqtt_broker_configs
from application.main.mqtt_connection.mqtt_client_connection import MqttClientConnection

def start():
    mqtt_client_connection = MqttClientConnection(
        mqtt_broker_configs['HOST'],
        mqtt_broker_configs['PORT'],
        mqtt_broker_configs['CLIENT_NAME'],
        mqtt_broker_configs.get('KEEPALIVE', 60),
        mqtt_broker_configs.get('USERNAME'),
        mqtt_broker_configs.get('PASSWORD')
    )
    mqtt_client_connection.start_connection()

    while True:
        time.sleep(0.001)
