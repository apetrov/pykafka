from confluent_kafka import Producer

p = Producer({'bootstrap.servers': 'kafka:9092'})

def push(p, message):
    p.produce('request', message.encode('utf-8'))

with(open("test.json")) as f:
    message = f.read()
    [push(p, message) for x in range(100000)]

