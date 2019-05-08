import sys
import socket
import select

HOST = '127.0.0.1'
SOCKET_LIST = []
RECV_BUFFER = 4096
PORT = 8989

def broadcast():

def messaging_server():
    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serv_sock.bind((HOST, PORT))
    serv_sock.listen(10)
    
    SOCKET_LIST.append(serv_sock)
    print("Messaging server started on port", str(PORT))
    
    while True:
        ready_to_read, ready_to_write, in_error = select.select(SOCKET_LIST, [], [], 0)
        for sock in ready_to_read:
            if sock == serv_sock:
                sockfd, addr = serv_sock.accept()
                SOCKET_LIST.append(sockfd)
                print("Client", addr, "connected to server")
'''             
                broadcast(serv_sock, sockfd, )
'''
            else:
                try:
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        # broadcast
                        pass
                    else:
                        if sock in SOCKET_LIST:
                            SOCKET_LIST.remove(sock)
                        #broadcast
                except:
                    # broadcast
                    continue
    serv_sock.close()
    
    
ready_to_read, ready_to_write, in_error = select.select(potential_readers, potential_writers, potential_errs, timeout)

