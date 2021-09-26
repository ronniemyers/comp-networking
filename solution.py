from socket import *
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(("", port))
    serverSocket.listen(1)

    while True:
        # Establish the connection
        # print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        try:

            try:
                message =  connectionSocket.recv(1024)
                filename = message.split()[1]
                f = open(filename[1:])
                outputdata = f.read()
                response = 'HTTP/1.1 200 OK\r\n'
                response += 'Content-Type: text/html\n'
                response += '\n'
                connectionSocket.send(response.encode())
                # Send one HTTP header line into socket.
                connectionSocket.send("HTTP/2 200 OK".encode())

                # Send the content of the requested file to the client
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())

                connectionSocket.send("\r\n".encode())
                connectionSocket.close()
            except IOError:
                connectionSocket.send("HTTP/2 404 NOT FOUND".encode())
                connectionSocket.close()

        except (ConnectionResetError, BrokenPipeError):
            pass

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webServer(13331)
