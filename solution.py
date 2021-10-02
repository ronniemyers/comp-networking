import sys
from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n First email"
    endmsg = "\r\n.\r\n"

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    recv = clientSocket.recv(1024).decode()
    if recv[:3] != '220':
        sys.exit()

    # Send HELO command and print server response.
    heloCommand = 'HELO Ronnie\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    if recv1[:3] != '250':
        sys.exit()
        # print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    fromCommand = 'MAIL FROM: <test@mail.com>\r\n'
    clientSocket.send(fromCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    if recv1[:3] != '250':
        sys.exit()
        # print('2. 250 reply not received from server.')

    # Send RCPT TO command and print server response.
    rcptCommand = 'RCPT TO: <test@protaski.com>\r\n'
    clientSocket.send(rcptCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    if recv1[:3] != '250':
        sys.exit()
        # print('3. 250 reply not received from server.')

    # Send DATA command and print server response.
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    if recv1[:3] != '354':
        sys.exit()
        # print('4. 354 reply not received from server.')

    # Send message data.
    data = msg
    clientSocket.send(data.encode())

    # Message ends with a single period.
    periodCommand = endmsg
    clientSocket.send(periodCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    if recv1[:3] != '250':
        sys.exit()
        # print('5. 250 reply not received from server.')

    # Send QUIT command and get server response.
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    if recv1[:3] != '221':
        sys.exit()
        # print('221 reply not received from server.')
    clientSocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')