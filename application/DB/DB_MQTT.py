import pymongo as pyM
from application.DB.passaword.DB_password import password_db

# Se conecta ao Mongo Atlas com parâmetros TLS
client = pyM.MongoClient(password_db)

# Cria o DB
db = client.mqtt

# Cria a coleção 'bank_collection'
collection = db.umc_collection