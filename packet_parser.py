import struct
import binascii

def parse_input_file(file_path):
    with open(file_path, 'r') as f:
        data = f.read().strip()
    # Convert hex dump into binary
    return binascii.unhexlify(data.replace(" ", "").replace("\n", ""))


# Parses the captured packet data to extract headers and payload.
def parse_packet(packet):
    
    # Parse the IP header (20 bytes for IPv4)
    ip_header = packet[:20]
    iph = struct.unpack("!BBHHHBBH4s4s", ip_header)
    #source: https://www.geeksforgeeks.org/introduction-and-ipv4-datagram-header/ 

    src_ip = '.'.join(map(str, iph[8]))
    dest_ip = '.'.join(map(str, iph[9]))
    protocol = iph[6]

    print(f"Source IP: {src_ip}, Destination IP: {dest_ip}, Protocol: {protocol}")

    # Parse the TCP header (20 bytes minimum)
    tcp_header = packet[20:40]
    tcph = struct.unpack("!HHLLBBHHH", tcp_header)
    src_port = tcph[0]
    dest_port = tcph[1]
    seq_num = tcph[2]
    ack_num = tcph[3]
    #source: https://www.geeksforgeeks.org/services-and-segment-structure-in-tcp/

    print(f"Source Port: {src_port}, Destination Port: {dest_port}, Sequence Number: {seq_num}, Acknowledgment Number: {ack_num}")

    # Extract payload
    payload = packet[40:]
    print(f"Payload: {payload.decode(errors='ignore')}")

    return ip_header, tcp_header, payload

def main():
    input_file = "packet.txt"  
    captured_data = parse_input_file(input_file)


    ip_header, tcp_header, payload = parse_packet(captured_data)


  

if __name__ == "__main__":
    main()
