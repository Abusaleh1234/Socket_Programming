import socket

def start_tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))  # Bind to localhost and port 12345
    server_socket.listen(1)  # Listen for incoming connections
    print("Server is listening on port 12345...")

    conn, addr = server_socket.accept()  # Accept a connection
    print(f"Connected to {addr}")

    try:
        while True:
            # Receive data from client
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f"Client: {data}")

            # Get response from server
            message = input("Server: ")
            conn.send(message.encode())
    except KeyboardInterrupt:
        print("Chat ended by user.")
    finally:
        conn.close()
        server_socket.close()

if __name__ == "__main__":
    start_tcp_server()
