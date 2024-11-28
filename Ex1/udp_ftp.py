import socket
import threading
import time

# Server code in a separate function
def udp_server(host='127.0.0.1', port=65433):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"UDP Server listening on {host}:{port}")

    with open("received_file_udp.txt", "wb") as file:
        while True:
            data, addr = server_socket.recvfrom(1024)
            if not data:
                break
            file.write(data)
            print(f"Received data from {addr} and data is {data.decode()}")

    print("File received successfully. Server shutting down.")

# Client code in a separate function
def udp_client(filename, host='127.0.0.1', port=65433):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    with open(filename, "rb") as file:
        for line in file:
            client_socket.sendto(line, (host, port))
            print(f"Sent: {line.decode()}")
            time.sleep(0.1)  # Brief delay to avoid overwhelming the server

    # Sending an empty byte to indicate the end of transmission
    client_socket.sendto(b'', (host, port))

    client_socket.close()
    print("File sent successfully.")

# Function to choose between server and client
def main():
    mode = input("Enter mode (server/client): ").strip().lower()
    if mode == "server":
        udp_server()
    elif mode == "client":
        filename = input("Enter the filename to send: ").strip()
        udp_client(filename)
    else:
        print("Invalid mode. Please enter either 'server' or 'client'.")

# Run the main function to choose between server and client mode
if __name__ == "__main__":
    main()
