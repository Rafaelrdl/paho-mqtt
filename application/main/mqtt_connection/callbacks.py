import json
import datetime
from application.DB.DB_MQTT import collection
from application.configs.broker_configs import mqtt_broker_configs

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Cliente conectado  com sucesso: {client}")
        client.subscribe(mqtt_broker_configs["TOPIC"])
    else:
        print(f"Erro de conexão com o servidor! codigo={rc}")

def on_subscribe(client, userdata, mid, granted_qos):
    print(f"Subscribed: {mqtt_broker_configs["TOPIC"]}")
    print(f"QOS: {granted_qos}")

def on_message(client, userdata, message):
    print('Mensagem recebida!')
    print(client)
    print(message.payload)

    try:
        #Convertendo o payload para String e depois para uma lista de dicionarios json
        payload_str = message.payload.decode("utf-8")
        payload_list = json.loads(payload_str)

        if isinstance(payload_list, list):
            for payload_dict in payload_list:
                #Adicionando um timestamp à mensagem
                payload_dict['timestamp'] = datetime.datetime.utcnow()
                #Inserindo a mensagem no MongoDB
                collection.insert_one(payload_dict)
                print(f"Mensagem salva no MongoDB: {payload_dict}")
        else:
            print("Formato de payload inesperado, não é uma lista.")
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")
    except Exception as e:
        print(f"Erro ao processar mensagem: {e}")
