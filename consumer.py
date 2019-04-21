from confluent_kafka import Consumer, KafkaError
import orjson



c = Consumer({
    'bootstrap.servers': 'kafka:9092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['request'])

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    data = orjson.loads(msg.value().decode('utf-8'))
    print('Got: {}'.format(len(data.keys())))

c.close()
