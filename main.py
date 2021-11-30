import socket
from threading import Thread, Lock
from queue import Queue

# Configure ports range, targeted host and number of thread
ports = range(1, 999)
host = "1.1.1.1"
threads_number = 200

# Var init
sock = socket
queue = Queue()
print_lock = Lock()


def port_scan(port):
    global sock
    try:
        # For each worker, open a socket connection
        sock = socket.socket()
        sock.connect((host, port))
    except socket.error:
        with print_lock:
            pass  # TODO : Implement a close statement
    else:
        with print_lock:
            print(f"{host:15}:{port:5} open")
    finally:
        sock.close()


def scan_thread():
    global queue
    while True:
        # Workers scheduler
        worker = queue.get()
        port_scan(worker)
        queue.task_done()


def main(host, ports):
    global queue
    for thread in range(threads_number):
        thread = Thread(target=scan_thread)
        thread.daemon = True
        thread.start()

    # For each ports, add a worker in the queue (modulo threads_number)
    for worker in ports:
        queue.put(worker)

    queue.join()


if __name__ == "__main__":
    main(host, ports)
