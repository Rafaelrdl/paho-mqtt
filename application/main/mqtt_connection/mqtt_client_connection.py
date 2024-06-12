import paho.mqtt.client as mqtt

class MqttClientConnection:
    def __init__(self, broker_ip: str, port: int, client_name: str, keepalive: int = 60, username: str = None, password: str = None):
        self.__broker_ip = broker_ip
        self.__port = port
        self.__client_name = client_name
        self.__keepalive = keepalive
        self.__username = username
        self.__password = password

    def start_connection(self):
        mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
        mqtt_client._client_id = self.__client_name.encode('utf-8')
        if self.__username and self.__password:
            mqtt_client.username_pw_set(self.__username, self.__password)
        mqtt_client.connect(host=self.__broker_ip, port=self.__port, keepalive=self.__keepalive)
        mqtt_client.loop_start()
