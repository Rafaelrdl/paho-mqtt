import paho.mqtt.client as mqtt

# Definir callbacks (de acordo com a nova API)
def on_connect(client, userdata, flags, reason_code, properties=None):
    print(f"Connected with reason code {reason_code}")

def on_publish(client, userdata, mid, properties=None, reason_code=None):
    print(f"Message published with mid {mid}")

# Criar o cliente MQTT usando a versão mais recente da API de callback
mqtt_client = mqtt.Client(client_id='meu_publisher', protocol=mqtt.MQTTv311)

# Definir nome de usuário e senha para autenticação
mqtt_client.username_pw_set(username='token', password='701db075-4325-46ba-97bd-0499d2a62412')

# Atribuir os callbacks
mqtt_client.on_connect = on_connect
mqtt_client.on_publish = on_publish

# Conectar ao broker MQTT
mqtt_client.connect(host='mqtt.tago.io', port=1883, keepalive=60)

# Publicar uma mensagem
mqtt_client.publish(topic="/teste/paho", payload="Testando daquele nipe")

