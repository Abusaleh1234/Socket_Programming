import socket

def start_tcp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))  # Connect to the server

    try:
        while True:
            # Get message from client user
            message = input("Client: ")
            client_socket.send(message.encode())

            # Receive response from server
            data = client_socket.recv(1024).decode()
            print(f"Server: {data}")
    except KeyboardInterrupt:
        print("Chat ended by user.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_tcp_client()
