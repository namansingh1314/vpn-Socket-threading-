import socket
import threading

#proxy server configurstion
proxy_host = '123.45.67.89'
proxy_port = 8888

#destination server configuration 
destination_host = 'google.com'
destination_port = 80

def handle_client(client_socket):
    #connect to destination server
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.connect((destination_host,destination_port))

    #forward data beween client and server 
    while True:
        #receive data from client
        client_data = client_socket.recv(4096)
        if len(client_data) == 0:
            break

        #forward data to the server
        server_socket.send(client_data)
    #close the connection
    client_socket.close()
    server_socket.close()


def start_proxy():
    #create a socket object
    proxy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #bind the socket to a host and part
    proxy.bind((proxy_host, proxy_port))
    #listen for incoming connections
    proxy.listen(5)

    print(f"Proxy server listening on {proxy_host}:{proxy_port}")

    while True:
        client_socket, addr =proxy.accept()
        print(f"Accepted connection from {addr[0]}: {addr[1]}")

        #start a new thread to handle client
        client_handle= threading.Thread(target=handle_client,args=(client_socket,))
        client_handle.start()


if __name__ == "__main__":
    start_proxy()