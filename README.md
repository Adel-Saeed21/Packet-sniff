# Packet-sniff
# HTTP Packet Sniffing Tool

This project is a packet sniffing tool built using Python and the `Scapy` library. It captures HTTP requests and can identify potential sensitive information like usernames or passwords sent over the network in plain text.

## Features

- **Packet Sniffing**: Captures HTTP requests on a specified network interface.
- **HTTP Request Detection**: Identifies and prints the requested host and path from the HTTP headers.
- **Credential Sniffing**: Looks for common keywords like "username," "password," or "email" in the packet data payload and alerts the user when found.

## How It Works

1. The user provides the network interface to sniff on via command line arguments.
2. The tool captures packets from the specified interface.
3. It processes each packet and checks if it contains an HTTP request.
4. If any sensitive data (like "username" or "password") is found in the HTTP request payload, the tool prints it as a potential credential leak.

## Prerequisites

- Python 3.x
- `Scapy` library
- Root or administrative privileges (required for packet sniffing)

## Installation

1. Install Python 3.x from [python.org](https://www.python.org/downloads/) if you don't have it installed.
2. Install Scapy by running:

   ```bash
   pip install scapy
