# DataCommunication-SocketProgramming


[Türkçe açıklama için aşağıya kaydırın / Scroll down for Turkish description]

This project is a comprehensive simulation of data communication systems, specifically focusing on socket programming and error detection algorithms. It implements a multi-layered architecture (Sender-Server-Receiver) to demonstrate how data travels through a network, how it can be corrupted, and how errors are identified.



## Technical Highlights
- **Communication Protocol:** Built using Python's `socket` library (TCP/IP).
- **Supported Detection Methods:**
  - **Parity Bit:** Even/Odd parity calculation.
  - **2D Parity:** Row and column based matrix parity.
  - **CRC16:** Cyclic Redundancy Check for high-reliability detection.
  - **Hamming Code:** Error detection using 4-bit block encoding.
  - **Internet Checksum:** Standard IP-based checksum implementation.
- **Graphical Interfaces:** Independent GUIs for Client 1 and Client 2 using `tkinter`.
- **Error Simulation:** The Server acts as a "Noisy Channel" by injecting random bit flips, character deletions, or burst errors.

## Architecture & Flow
1. **Client 1 (Sender):** Encapsulates data into a packet: `DATA | METHOD | CONTROL`.
2. **Server (The Channel):** Receives the packet on port 9000, applies a random error method, and forwards it to the receiver.
3. **Client 2 (Receiver):** Listens on port 9001, re-calculates the control bits, and alerts if the data is "CORRUPTED" or "CORRECT".

## Execution Order
1. `python client2_ui.py` (Starts listening)
2. `python server.py` (Starts the middleman)
3. `python client1_ui.py` (Sends the data)

---

# DataCommunication-SocketProgramming (Türkçe)

Bu proje, soket programlama ve hata tespit algoritmaları üzerine odaklanmış kapsamlı bir veri haberleşmesi simülasyonudur. Verinin ağ üzerindeki yolculuğunu, iletim sırasında nasıl bozulabileceğini ve bu hataların nasıl tespit edildiğini gösteren üç katmanlı (Gönderici-Sunucu-Alıcı) bir yapı sunar.

## Teknik Özellikler
- **Haberleşme Protokolü:** Python `socket` kütüphanesi ile TCP/IP üzerinden iletişim sağlanır.
- **Hata Tespit Yöntemleri:**
  - **Parity:** Tek/Çift parite hesabı.
  - **2D Parity:** Matris tabanlı satır ve sütun kontrolü.
  - **CRC16:** Döngüsel Yinelemeli Kontrol.
  - **Hamming Code:** 4-bit blok kodlama yöntemi.
  - **Internet Checksum:** Standart internet sağlama toplamı.
- **Görsel Arayüzler:** `tkinter` kullanılarak geliştirilmiş kullanıcı dostu Gönderici ve Alıcı panelleri.
- **Hata Simülasyonu:** Sunucu, gerçek hayattaki "gürültülü kanal" (noisy channel) gibi davranarak veriyi rastgele bozar (bit flip, karakter silme, burst error vb.).

## Çalışma Mantığı
1. **Client 1 (Gönderici):** Kullanıcı verisini alır, algoritmayı uygular ve `VERI | METOT | KONTROL` formatında paketler.
2. **Server (Kanal):** 9000 portunu dinler, gelen veriyi bozar ve alıcıya iletir.
3. **Client 2 (Alıcı):** 9001 portundan gelen paketi açar, kontrol bitlerini tekrar hesaplar ve durumu "DOĞRU" veya "BOZUK" olarak raporlar.

## Çalıştırma Talimatı
Sırasıyla terminallerde şu dosyaları çalıştırın:
1. `python client2_ui.py`
2. `python server.py`
3. `python client1_ui.py`
