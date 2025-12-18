import socket
import threading
import tkinter as tk
from tkinter import ttk
from client1 import generate_control

HOST = "127.0.0.1"
PORT = 9001

# --- SERVER THREAD ---
def start_listener(log_box, status_var):
    s = socket.socket()
    s.bind((HOST, PORT))
    s.listen()

    log_box.insert(tk.END, "Client 2 listening on 127.0.0.1:9001\n")
    log_box.see(tk.END)

    while True:
        c, addr = s.accept()
        packet = c.recv(4096).decode()

        try:
            data, method, incoming = packet.split("|")
            computed = generate_control(data, method)

            log_box.insert(tk.END, "\n--- RECEIVED PACKET ---\n")
            log_box.insert(tk.END, f"Data: {data}\n")
            log_box.insert(tk.END, f"Method: {method}\n")
            log_box.insert(tk.END, f"Sent Check Bits: {incoming}\n")
            log_box.insert(tk.END, f"Computed Check Bits: {computed}\n")

            if computed == incoming:
                status_var.set("DATA CORRECT")
                log_box.insert(tk.END, "Status: DATA CORRECT\n")
            else:
                status_var.set("DATA CORRUPTED")
                log_box.insert(tk.END, "Status: DATA CORRUPTED\n")
        except Exception as e:
            log_box.insert(tk.END, f"Error: {e}\n")

        log_box.see(tk.END)
        c.close()

# --- UI ---
root = tk.Tk()
root.title("Error Control Simulator - Client 2")
root.geometry("600x400")

frame = ttk.Frame(root, padding=10)
frame.pack(fill="both", expand=True)

label = ttk.Label(frame, text="Receiver (Client 2)", font=("Arial", 14, "bold"))
label.pack(pady=5)

status_var = tk.StringVar(value="WAITING")
status_label = ttk.Label(frame, textvariable=status_var, font=("Arial", 12))
status_label.pack(pady=5)

log_box = tk.Text(frame, height=15)
log_box.pack(fill="both", expand=True)

# Start server thread
threading.Thread(target=start_listener, args=(log_box, status_var), daemon=True).start()

root.mainloop()
