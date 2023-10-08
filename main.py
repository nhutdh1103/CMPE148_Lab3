from socket import *
import base64
import ssl
import time
from pip._vendor.distlib.compat import raw_input

msg = "\r\n I love computer networks!" 
endmsg = "\r\n.\r\n"

username =  "ladybugs@gmail.com"
password = "123456"
email_to = "dohoangnhu.tran@sjsu.edu" # recepient email account

def main():
    
# Choose a mail server (e.g. Google mail server) and call it mailserver mailserver
# #Fill in start 
    MailServer = "smtp.freesmtpservers.com"
    MailPort = 25
    serverPort = (MailServer, MailPort)

# #Fill in end

# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start

    clientSocket = socket (AF_INET, SOCK_STREAM)
    clientSocket.connect(serverPort)

#Fill in end

    recv = clientSocket.recv(1024).decode() 
    print("Message after connection request: ", recv)

    if recv[:3] != '220':\
        print('220 reply not received from server.\n')

# Send HELO command and print server response. 
    heloCommand = 'HELO Alice\r\n' 
    clientSocket.send(heloCommand.encode())

    recv1 = clientSocket.recv(1024).decode() 

    print("\nSend HELO command and print server response:", recv1)

    if recv1[:3] != '250':
        print('250 reply not received from server.\n')

    base64_str = ("\x00"+username+"\x00"+password).encode()
    base64_str = base64.b64encode(base64_str)
    authMsg = "AUTH PLAIN ".encode()+base64_str+"\r\n".encode()
    clientSocket.send(authMsg)
    recv_auth = clientSocket.recv(1024)
    print(recv_auth.decode())


# Send MAIL FROM command and print server response.
# Fill in start

    mailFrom = "MAIL FROM:<{}>\r\n".format(username)
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024)
    recv2 = recv2.decode()
    print("Server respond to MAIL FROM: "+recv2)

# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
    rcptTo = "RCPT TO:<{}>\r\n".format(email_to)
    clientSocket.send(rcptTo.encode())
    recv3 = clientSocket.recv(1024)
    recv3 = recv3.decode()
    print("Server respond to RCPT TO: "+recv3)

# Fill in end

# Send DATA command and print server response.
# Fill in start

    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    recv4 = clientSocket.recv(1024)
    print("After DATA command: ", recv4.decode())
    if recv1[:3] != '250':
        print('250 reply not received from server.\n')

# Fill in end

# Send message data.
# Fill in start

    subject = "Subject: SMTP mail client testing \r\n\r\n"
    clientSocket.send(subject.encode())

    message = raw_input("Enter message here: \r\n")


# Fill in end

# Message ends with a single period.
# Fill in start

    mailEndMsg = "\r\n.\r\n"
    clientSocket.send(message.encode())
    clientSocket.send(mailEndMsg.encode())

    recv5 = clientSocket.recv(1024)
    print("Response after sending message body:", recv5.decode())

# Fill in end
# Send QUIT command and get server response.
# Fill in start
    quitCommand = "QUIT\r\n"
    clientSocket.send(quitCommand.encode())
    recv6 = clientSocket.recv(1024)
    print(recv6.decode())
    print(quitCommand)
# Fill in end
    clientSocket.close()

    if __name__ == '__main__':
        main()