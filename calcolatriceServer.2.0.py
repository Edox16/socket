import socket
from threading import Thread

SERVER_ADDRESS='127.0.0.1'
SERVER_PORT=22224

def ricevi_comandi(sock_service, addr_client):
    print("avviato")
    while True:
        pass
        #da scrivere

        sock_service.close()

def ricevi_connessioni(sock_listen):
    while True:
        sock_service, addr_client=sock_listen.accepts()
        print("\nConnessione ricevuta da "+str(addr_client))
        print("\nCreo un thread per servire le richieste ")
        try:
            Thread(target=ricevi_comandi, args=(sock_service, addr_client)).start()
        except:
            print("il thread non si avvia ")
            sock_listen.close()

def avvia_server(indirizzo, porta):
    sock_listen=socket.socket()
    sock_listen.setsockopt(socket.SQL_SOCKET, socket.SO_REUSEADDR, 1)
    sock_listen.bind((SERVER_ADDRESS, SERVER_PORT))
    sock_listen.listen(5)
    print("Server in ascolto su %s." % str((SERVER_ADDRESS, SERVER_PORT)))
    ricevi_connessioni(sock_listen)

if __name__=='__main__':
    avvia_server(SERVER_ADDRESS, SERVER_PORT)