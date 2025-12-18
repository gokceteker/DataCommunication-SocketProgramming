import socket
import tkinter as tk
from tkinter import ttk, messagebox
from client1 import generate_control

# --- UI CLIENT ---
def send_packet():
    data = entry_text.get()
    method = method_var.get()

    if not data:
        messagebox.showerror("Error", "Please enter text")
        return

    control = generate_control(data, method)
    packet = f"{data}|{method}|{control}"

    try:
        s = socket.socket()
        s.connect(("127.0.0.1", 9000))
        s.send(packet.encode())
        s.close()
        result_var.set(f"Sent: {packet}")
    except Exception as e:
        messagebox.showerror("Connection Error", str(e))

# --- MAIN WINDOW ---
root = tk.Tk()
root.title("Error Control Simulator - Client 1")
root.geometry("500x300")

# Text input
frame = ttk.Frame(root, padding=15)
frame.pack(fill="both", expand=True)

label1 = ttk.Label(frame, text="Enter Text:")
label1.pack(anchor="w")

entry_text = ttk.Entry(frame, width=50)
entry_text.pack(pady=5)

# Method selection
label2 = ttk.Label(frame, text="Choose Error Control Method:")
label2.pack(anchor="w", pady=(10, 0))

method_var = tk.StringVar(value="CRC16")
methods = ["PARITY", "2DPARITY", "CRC16", "HAMMING", "CHECKSUM"]

combo = ttk.Combobox(frame, values=methods, textvariable=method_var, state="readonly")
combo.pack(pady=5)

# Send button
send_btn = ttk.Button(frame, text="Send Packet", command=send_packet)
send_btn.pack(pady=10)

# Result label
result_var = tk.StringVar()
result_label = ttk.Label(frame, textvariable=result_var, wraplength=450)
result_label.pack(pady=10)

root.mainloop()
