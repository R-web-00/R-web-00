import socket

def main():
    try:
        # Create a socket object
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('localhost', 3000))  # Bind to port 6666
        server_socket.listen(1)  # Listen for incoming connections
        print("Server is listening on port 6666...")

        # Accept a connection
        client_socket, addr = server_socket.accept()
        print(f"Connected by {addr}")

        # Receive data (UTF-8 encoded)
        message = client_socket.recv(1024).decode('utf-8')
        print(f"message= {message}")

        # Close the sockets
        client_socket.close()
        server_socket.close()

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
