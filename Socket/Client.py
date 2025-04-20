import socket

def main():
       
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 3000))

        
        message = "Welcome to DC Practicals"
        client_socket.sendall(message.encode('utf-8'))

        
        client_socket.close()

if __name__ == "__main__":
    main()

#Conclusion
#Socket programming enables IPC by allowing processes to communicate over a network or locally.
#Unlike pipes, message queues, and shared memory, sockets support cross-machine communication 
#and scalability, making them ideal for distributed systems.
