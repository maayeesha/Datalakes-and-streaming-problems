"""
pipeline.py
----------------
This file launches BOTH producer and consumer using Python threads to simulate
a real streaming pipeline.

"""

import threading
from queue import Queue
from producer import CSVProducer
from consumer import Consumer

def main():
    """
    TODO:
    - Create the shared queue.
    - Instantiate the producer and consumer.
    - Create a thread for each.
    - Start both threads.
    - Optionally join them so the program runs continuously.

    The students should run:
        python pipeline.py
    and observe live streaming behavior.
    """
    shared_queue = Queue()
    producer = CSVProducer('Python-Streaming-Lab\\transactions.csv', shared_queue, delay=1.0)
    consumer = Consumer(shared_queue)
    thread_p = threading.Thread(target=producer.start)
    thread_c = threading.Thread(target=consumer.start)
    thread_p.start()
    thread_c.start()

    thread_p.join()
    shared_queue.put(None)  #exitting
    thread_c.join()

if __name__ == "__main__":
    print("Starting the Python Streaming Pipeline")
    main()