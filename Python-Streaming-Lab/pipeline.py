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
    q = Queue()
    producer = CSVProducer('Python-Streaming-Lab\\transactions.csv', q, delay=1.0)
    consumer = Consumer(q)
    thread_p = threading.Thread(target=producer.start)
    thread_c = threading.Thread(target=consumer.start)
    


if __name__ == "__main__":
    print("Starting the Python Streaming Pipeline...")
    main()
