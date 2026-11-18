import socket

HOST = "localhost"
PORT = 9999

# Create socket
server_socket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM
)

# Bind socket to host and port
server_socket.bind((HOST, PORT))

# Listen for connection
server_socket.listen(1)

print("======================================")
print("Socket Server Started")
print("Waiting for Spark to connect...")
print("Host:", HOST)
print("Port:", PORT)
print("======================================")

# Accept connection from Spark
connection, address = server_socket.accept()

print("Spark connected!")
print("Start entering messages.")
print("Type 'exit' to stop.")
print("--------------------------------------")

while True:
    message = input("Enter message: ")

    if message.lower() == "exit":
        break

    # Send message to Spark
    connection.sendall(
        (message + "\n").encode("utf-8")
    )

print("Closing connection...")

connection.close()
server_socket.close()

print("Socket server stopped.")