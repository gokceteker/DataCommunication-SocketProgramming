import socket
import random
import binascii

# ---------------- PARITY ----------------
def parity_bit(text, mode="even"):
    bits = ''.join(format(ord(c), '08b') for c in text)
    ones = bits.count("1")
    if mode == "even":
        return "0" if ones % 2 == 0 else "1"
    else:
        return "1" if ones % 2 == 0 else "0"

# ---------------- 2D PARITY ----------------
def matrix_parity(text):
    bits = ''.join(format(ord(c), '08b') for c in text)
    if len(bits) % 8 != 0:
        bits += "0" * (8 - len(bits) % 8)

    matrix = [bits[i:i+8] for i in range(0, len(bits), 8)]

    row_parity = ''.join(str(row.count("1") % 2) for row in matrix)

    col_parity = ""
    for col in range(8):
        col_bits = "".join(row[col] for row in matrix)
        col_parity += str(col_bits.count("1") % 2)

    return row_parity + ":" + col_parity

# ---------------- CRC16 ----------------
def crc16(text):
    data = bytearray(text.encode())
    poly = 0x1021
    crc = 0xFFFF

    for byte in data:
        crc ^= byte << 8
        for _ in range(8):
            crc = (crc << 1) ^ poly if (crc & 0x8000) else (crc << 1)
            crc &= 0xFFFF

    return format(crc, '04X')

# ---------------- HAMMING ----------------
def hamming_encode_4bit(data_bits):
    d = list(map(int, data_bits))
    p1 = (d[0] + d[1] + d[3]) % 2
    p2 = (d[0] + d[2] + d[3]) % 2
    p3 = (d[1] + d[2] + d[3]) % 2
    return f"{p1}{p2}{d[0]}{p3}{d[1]}{d[2]}{d[3]}"

def hamming(text):
    bits = ''.join(format(ord(c), '08b') for c in text)
    encoded = ""
    for i in range(0, len(bits), 4):
        block = bits[i:i+4].ljust(4, "0")
        encoded += hamming_encode_4bit(block)
    return encoded

# ---------------- Internet Checksum ----------------
def internet_checksum(text):
    data = text.encode()
    if len(data) % 2 == 1:
        data += b'\x00'

    checksum = 0
    for i in range(0, len(data), 2):
        word = (data[i] << 8) + data[i+1]
        checksum += word
        checksum = (checksum & 0xFFFF) + (checksum >> 16)

    checksum = ~checksum & 0xFFFF
    return format(checksum, "04X")


# MAIN CLIENT 1
def generate_control(text, method):
    if method == "PARITY":
        return parity_bit(text)
    elif method == "2DPARITY":
        return matrix_parity(text)
    elif method == "CRC16":
        return crc16(text)
    elif method == "HAMMING":
        return hamming(text)
    elif method == "CHECKSUM":
        return internet_checksum(text)

def main():
    s = socket.socket()
    s.connect(("127.0.0.1", 9000))

    data = input("Enter text: ")

    print("Choose method:\n1-Parity\n2-2D Parity\n3-CRC16\n4-Hamming\n5-Checksum")
    choice = input("Method: ")

    methods = {
        "1": "PARITY",
        "2": "2DPARITY",
        "3": "CRC16",
        "4": "HAMMING",
        "5": "CHECKSUM"
    }

    method = methods.get(choice, "CRC16")
    control = generate_control(data, method)

    packet = f"{data}|{method}|{control}"
    print("Sent Packet:", packet)

    s.send(packet.encode())
    s.close()

if __name__ == "__main__":
    main()
