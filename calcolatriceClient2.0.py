import socket

SERVER_ADDRESS='127.0.0.1'
SERVER_PORT=22224

def invia_comandi(sock_service):
    while True:
        #pass poi è da eliminare
        pass
        #da scrivere

def  connessione_server(address, port):
    sock_service=socket.socket()
    sock_service.connect((SERVER_ADDRESS, SERVER_PORT))
    print("Connesso a " + str((SERVER_ADDRESS, SERVER_PORT)))
    invia_comandi(sock_service)

if __name__=='__main__':
    connessione_server(SERVER_ADDRESS, SERVER_PORT)