import socket
import random
import string

def bit_flip(text):
    bits = list(''.join(format(ord(c), "08b") for c in text))
    i = random.randint(0, len(bits)-1)
    bits[i] = "1" if bits[i] == "0" else "0"

    new = "".join(bits)
    return ''.join(chr(int(new[i:i+8], 2)) for i in range(0, len(new), 8))

def substitute_char(text):
    i = random.randint(0, len(text)-1)
    return text[:i] + random.choice(string.ascii_letters) + text[i+1:]

def delete_char(text):
    if len(text) <= 1: return text
    i = random.randint(0, len(text)-1)
    return text[:i] + text[i+1:]

def insert_char(text):
    i = random.randint(0, len(text))
    return text[:i] + random.choice(string.ascii_letters) + text[i:]

def swap_chars(text):
    if len(text) < 2: return text
    i = random.randint(0, len(text)-2)
    return text[:i] + text[i+1] + text[i] + text[i+2:]

def burst_error(text):
    if len(text) < 3: return text
    start = random.randint(0, len(text)-3)
    burst = "".join(random.choice(string.ascii_letters) for _ in range(3))
    return text[:start] + burst + text[start+3:]

errors = [bit_flip, substitute_char, delete_char, insert_char, swap_chars, burst_error]

def main():
    s = socket.socket()
    s.bind(("127.0.0.1", 9000))
    s.listen()

    print("Server running...")

    while True:
        try:
            c, addr = s.accept()
            packet = c.recv(4096).decode()
            
            if not packet:
                continue

            # split("|", 2) sayesinde paket içinde fazladan | olsa bile hata vermez
            data, method, control = packet.split("|", 2) 

            corrupt = random.choice(errors)
            corrupted_data = corrupt(data)

            new_packet = f"{corrupted_data}|{method}|{control}"
            print(f"Gelen: {packet} -> Gönderilen: {new_packet}")

            # Client 2'ye ilet
            receiver = socket.socket()
            receiver.settimeout(2) # Bağlantı beklerken takılmaması için
            receiver.connect(("127.0.0.1", 9001))
            receiver.send(new_packet.encode())
            receiver.close()

            c.close()
            
        except Exception as e:
            print(f"Bir paket işlenirken hata oluştu: {e}")
            # Hata olsa bile döngü devam eder, sunucu kapanmaz
            if 'c' in locals(): c.close() 

if __name__ == "__main__":
    main()
