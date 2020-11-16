#Brokers using rabbitmq and pika 

This project, has used python classes and python methods to obtain two python scripts, that respectively runs a producer and a consumer . 
I have implemented this creating my own implementation of a `Producer` and `Consumer` class.
I have created separate functions for using different approaches like `fanout` and `topics`.
We could have used `apache kafka` for this also, which has a bit more extensive ecosystem, and would allow us to scale easier, when handling for larger amounts of data.
If we had several services running simultaneously typically implemented in a SOA (service oriented architecture).

We implemented this using `rabbitmq`, which has high performance using the ampq protocol. We have used the pika library using a `BlockingConnection` instance. This is interesting, when we inspect, the functions, that are inside the `callback_handler`, here we use the `input()` function, to get the user input(<i>in a real life scenario, this could simulate a client</i>). The consumer blocks while waiting for user input, which indicate, that we are using a message broker, because the consumer is running on a single thread, and therefore is blocking before each request is handled. 
<br />

Meanwhile we cna have mutiple producers, adding request to our queue, and we could also scale our consumer accordingly for bigger workloads. 

We can use a routing key to access specific queue's through the exchange or we could use the fanout approach to access all queues, that the producer knows about.

Check out the `callback_handler` file, to see our implementation of our business logic. The functionality is just mocked, but the implementation of the `Producer` and `Consumer` class provides a baseline on how to create an actual implementation. 