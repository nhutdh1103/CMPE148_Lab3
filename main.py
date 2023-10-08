from socket import *

msg = "\r\n I love computer networks!" 
endmsg = "\r\n.\r\n"

    
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


# Send MAIL FROM command and print server response.
# Fill in start

mailFrom = "MAIL FROM: <ladybugs@gmail.com>\r\n"
recv2 = clientSocket.recv(1024)
recv2 = recv2.decode()
print("Server respond to MAIL FROM: ", recv2)
if recv2[:2] != '250':
    print('250 reply not received from the server')

# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
rcptTo = "RCPT TO: <dohoangnhu.tran@sjsu.edu>\r\n"
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024)
recv3 = recv3.decode()
print("Server respond to RCPT TO: ", recv3)
if recv3[:3] != '250':
    print('250 reply not received from the server')
# Fill in end

# Send DATA command and print server response.
# Fill in start

dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024)
print("After DATA command: ", recv4.decode())
if recv4[:3] != '250':
    print('250 reply not received from server.\n')

# Fill in end

# Send message data.
# Fill in start

clientSocket.send(msg.encode())


# Fill in end

# Message ends with a single period.
# Fill in start

clientSocket.send(endmsg.encode())

# Fill in end
# Send QUIT command and get server response.
# Fill in start
quitCommand = "QUIT\r\n"
clientSocket.send(quitCommand.encode())
recv5 = clientSocket.recv(1024)
print(recv5.decode())
print(quitCommand)
if recv5[:3] != '221':
    print('221 reply not received from the server')
# Fill in end

clientSocket.close()
