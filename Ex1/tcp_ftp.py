import socket
import threading
import time

# TCP Server Function
def tcp_server(host='127.0.0.1', port=65432):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"TCP Server listening on {host}:{port}...")

    conn, addr = server_socket.accept()
    print(f"Connection established with {addr}")

    # Receive file in chunks of 100 bytes
    with open("received_file_tcp.txt", "wb") as file:
        while True:
            data = conn.recv(100)  # Receive 100 bytes
            if not data:
                break  # Stop when no data is received (client closed connection)
            file.write(data)
            conn.sendall(b"ACK")  # Send acknowledgment for the received chunk

    conn.close()
    server_socket.close()
    print("File received successfully. Server shutting down.")

# TCP Client Function
def tcp_client(filename, host='127.0.0.1', port=65432):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    # Read the file and send it in chunks of 100 bytes
    with open(filename, "rb") as file:
        while True:
            chunk = file.read(100)  # Read 100 bytes
            if not chunk:
                break  # Stop when the file is fully read
            client_socket.sendall(chunk)

            # Wait for acknowledgment with a timeout
            client_socket.settimeout(2.0)  # Set a timeout of 2 seconds
            try:
                ack = client_socket.recv(1024)
                if ack != b"ACK":
                    raise Exception("Did not receive proper acknowledgment.")
            except (socket.timeout, Exception) as e:
                print(f"Timeout/Error: {e}, retransmitting...")
                client_socket.sendall(chunk)  # Retransmit the same chunk

    client_socket.close()
    print("File sent successfully.")

# Function to choose between server and client
def main():
    mode = input("Enter mode (server/client): ").strip().lower()
    if mode == "server":
        tcp_server()
    elif mode == "client":
        filename = input("Enter the filename to send: ").strip()
        tcp_client(filename)
    else:
        print("Invalid mode. Please enter either 'server' or 'client'.")

# Run the main function to choose between server and client mode
if __name__ == "__main__":
    main()
