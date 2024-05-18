# Simple Proxy Server

This project is a simple TCP proxy server implemented in Python. It forwards data between a client and a destination server, acting as an intermediary.

## Table of Contents
- [Requirements](#requirements)
- [Configuration](#configuration)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Notes](#notes)

## Requirements

- Python 3.x
- `socket` library (standard library in Python)
- `threading` library (standard library in Python)

## Configuration

The proxy server and the destination server configurations are set within the script:

- **Proxy Server Configuration:**
  - `proxy_host`: IP address of the proxy server (default: '127.0.0.1')
  - `proxy_port`: Port on which the proxy server listens (default: 8888)

- **Destination Server Configuration:**
  - `destination_host`: Hostname of the destination server (default: 'google.com')
  - `destination_port`: Port of the destination server (default: 80)

These values can be modified in the script according to your requirements.

## Usage

1. **Clone the repository or download the script.**

2. **Modify the configuration** (if needed):
   ```python
   proxy_host = '127.0.0.1'
   proxy_port = 8888

   destination_host = 'google.com'
   destination_port = 80
   ```

3. **Run the proxy server**:
   ```bash
   python proxy_server.py
   ```

4. **Connect a client** to the proxy server using the proxy server's IP address and port.

## How It Works

1. **Initialize the Proxy Server:**
   - A socket object is created and bound to the specified `proxy_host` and `proxy_port`.
   - The server listens for incoming connections.

2. **Handle Client Connections:**
   - When a client connects, a new thread is started to handle the client connection.
   - The `handle_client` function connects to the destination server and forwards data between the client and the destination server.
   - Data is continuously received from the client and sent to the destination server until the connection is closed.

3. **Close Connections:**
   - Both the client and server sockets are closed once the data transmission is complete or if there is no more data to forward.

## Notes

- This is a simple implementation and does not include error handling, logging, or advanced proxy features.
- This proxy server does not support HTTPS. For HTTPS support, additional steps such as handling SSL/TLS encryption are required.
- Be cautious when using this proxy server in a production environment. Proper security measures and error handling should be implemented.

This basic proxy server is intended for educational purposes and simple use cases. For more robust and secure proxy server implementations, consider using established software or libraries.
