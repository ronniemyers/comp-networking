# Assignment 2
from socket import *
import sys
from email.parser import BytesParser
import pprint

HOST = "127.0.0.1"
PORT = 13331

def webServer(port=PORT):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serverSocket.bind((HOST, PORT))
    serverSocket.listen(1)

    while True:
        connectionSocket, addr = serverSocket.accept()
        try:
            message = connectionSocket.recv(1024)
            _, headers = message.split(b'\r\n', 1)
            header_bytes = BytesParser().parsebytes(headers)
            headers = dict(header_bytes.items())
            filename = message.split()[1]
            # print('File requested: %s\n' % filename.decode())
            # print('Request Headers:\n')
            pprint.pprint(headers, width=200)
            f = open(filename[1:])
            outputdata = f.read()
            res = 'HTTP/3 200 OK\r\n'
            res += 'Content-Type: text/html\n'
            res += '\n'
            connectionSocket.send(res.encode())

            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send('\r\n'.encode())
            response_message = '\nSuccess: HTTP/3 200 OK\n'
            # print(response_message)
            serverSocket.close()
        except IOError:
            response_message = '\nFailure: HTTP/3 404 NOT FOUND\n'
            connectionSocket.send('HTTP/3 404 NOT FOUND'.encode())
            # print(response_message)
            serverSocket.close()

        except (ConnectionResetError, BrokenPipeError):
            pass

        serverSocket.close()
        sys.exit()

if __name__ == "__main__":
    webServer(13331)
