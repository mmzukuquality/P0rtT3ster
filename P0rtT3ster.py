import socket
import sys

print("[*] Plez 1nput inform4tion of P0rt T3st...")
cliIP = input("[*] Client IP: ")
cliPort = input("[*] Client Port: ")

srvIP = input("[*] Server IP: ")
srvPort = input("[*] Server Port: ")

if (cliIP is "" or cliPort is "" or srvIP is "" or srvPort is ""):
	sys.exit(0)

print("[*] S3lect TCP or UDP")
p = input("[*] Protocol(t or u): ")

# TCP Test
if (p is "t"):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((cliIP, int(cliPort)))

	s.connect((srvIP, int(srvPort)))
	s.send(b"////// TCP P0rt T3st M3ss4g3 //////")
	print("[*] Send t3st M3ss4ge")
	s.close()

# UDP Test
elif (p is "u"):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((cliIP, int(cliPort)))

	s.sendto(b"////// UDP P0rt T3st M3ss4g3//////", (srvIP, int(srvPort)))
	print("[*] Send t3st M3ss4ge")
	s.close()
	
else:
	print("No Method...")