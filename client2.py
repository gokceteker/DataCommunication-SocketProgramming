import socket
from client1 import generate_control

def main():
    s = socket.socket()
    s.bind(("127.0.0.1", 9001))
    s.listen()

    print("Client 2 Waiting...")

    while True:
        c, addr = s.accept()
        packet = c.recv(4096).decode()

        data, method, incoming = packet.split("|")

        computed = generate_control(data, method)

        print("\n--- RECEIVED PACKET ---")
        print("Received Data:", data)
        print("Method:", method)
        print("Sent Check Bits:", incoming)
        print("Computed Check Bits:", computed)

        if computed == incoming:
            print("Status: DATA CORRECT")
        else:
            print("Status: DATA CORRUPTED\n")

        c.close()

if __name__ == "__main__":
    main()
