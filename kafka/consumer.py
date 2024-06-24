# importing the required modules  
from json import loads  
from kafka import KafkaConsumer  
# from pymongo import MongoClient  
# my_client = MongoClient('localhost : 27017')  
# my_collection = my_client.testnum.testnum  

# generating the Kafka Consumer  
my_consumer = KafkaConsumer(  
    'testnum',  
     bootstrap_servers = ['localhost : 9092'],  
     auto_offset_reset = 'earliest',  
     enable_auto_commit = True,  
     group_id = 'my-group',  
     value_deserializer = lambda x : loads(x.decode('utf-8'))  
     )  
for message in my_consumer:  
    message = message.value  
    # collection.insert_one(message)  
    # print(message + " added to " + my_collection)
    print(f"Message: {message}") 
    with open("text.txt", "w+") as f:
        f.write(str(message)) 