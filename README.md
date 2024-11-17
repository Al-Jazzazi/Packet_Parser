# Packet_Parser

**Packet_Parser** is a Python-based tool designed to take a single captured packet (in binary or hexadecimal format) and parse it into its constituent components. This tool helps you analyze network traffic by breaking down headers and payloads at various layers (e.g., IP, TCP/UDP, HTTP).

---

## Features
- Parses **one packet** at a time for detailed analysis.
- Supports:
  - IPv4 headers
  - TCP and UDP headers
  - Application layer payloads (e.g., HTTP data)
- Displays fields like source/destination IP, ports, protocol, and payload content.
- Reconstructs the packet from parsed components for further use.

---

## How It Works
1. Takes the raw packet data from a file (hexadecimal format expected).
2. Parses and decodes:
   - **Network layer (IPv4)**: Extracts source and destination IP addresses, TTL, and protocol.
   - **Transport layer (TCP/UDP)**: Extracts ports, sequence numbers, and flags.
   - **Application layer**: Displays readable payload data (e.g., HTTP requests).
3. Outputs the parsed fields and reconstructed packet.

---

## Input File Format
The input file should contain a **hexadecimal dump** of one captured packet. For example:

### Example Input: (I attached it in project under packet.txt)
Generated example by chatgpt 
```
4500003c1c4640004006b1e6c0a80002c0a80001
c38a0050abcd1234dcba567801123456abcdabcd
474554202f696e6465782e68746d6c20485454502f312e310d0a486f73743a207777772e6578616d706c652e636f6d0d0a0d0a
```

---

## Usage

1. Place the packet dump in a text file (e.g., `packet.txt`).
2. Run the script:
   ```bash
   python3 packet_parser.py
   ```
3. The program will:
   - Parse the packet fields.
   - Display the extracted data in a readable format.
   - Optionally save the reconstructed packet to a binary file.

---

## Output Example
### Console Output:
```
Source IP: 192.168.0.2, Destination IP: 192.168.0.1, Protocol: 6
Source Port: 50058, Destination Port: 80, Sequence Number: 2882343476, Acknowledgment Number: 3703199352
Payload: GET /index.html HTTP/1.1
Host: www.example.com
```

## Requirements
- Python 3.x
- Libraries:
  - `struct`
  - `binascii`

---

## Future Features
- Support for additional protocols (e.g., IPv6, ICMP).
- Batch parsing of multiple packets.
- Visualization of packet structures.


