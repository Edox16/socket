import socket
from threading import Thread
import json

from calcoloServerMulti import ricevi_comandi

SERVER_ADDRESS='127.0.0.1'
SERVER_PORT=22225

class Server():
    """
        Questa classe rappresenta un server
    """
    def __init__(self, address, port):
        self.address=address
        self.port=port
    
    def avvia_server(self):
        """
            Metodo per aprirsi e mettersi in ascolto aspettando richieste da servire
        """
        sock_listen=socket.socket()
        sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock_listen.bind((SERVER_ADDRESS, SERVER_PORT))
        #Sequnze di istruzioni che indicano l'avvio dell'ascolto
        sock_listen.listen(5)
        print("Server in ascolto su %s." % str((SERVER_ADDRESS, SERVER_PORT)))
        return sock_listen

    def accetta_connessioni(self, sock_listen):
        """
            Metodo per accettare richieste di servizio ed assegnare un Thread ad ognuna di esse
        """
        #Ciclo While che continua a girare sino a che il valore continua a rimanere True
        while True:
            sock_service, addr_client=sock_listen.accept()
        #Visualizzo due print, in cui creo dei thread per eseguire le mie operazioni
            print("\nConnessione ricevuta da "+str(addr_client))
            print("\nCreo un thread per servire le richieste ")
        #Funzioni try e except, con successivo controllo degli errori
            try:
                Thread(target=self.ricevi_comandi, args=(sock_service, addr_client)).start()
            except:
                print("il thread non si avvia ")
                sock_listen.close()

    def ricevi_comandi(self, sock_service, addr_client):
        """
            Metodo per ricevere i comandi e servire le richieste ricevute
        """
        while True:
            data=sock_service.recv(1024)
            if not data: #se data è un vettore vuoto risulta false; sennò true/if len(data)==0/se è vuoto esce, sennò continua
                break
            #Istruzione data a cui passo i dati, e dopo faccio la stessa cosa
            #creando tre variabili a cui passo rispettivamente solo "primoNumero", "operazione" e, infine, secondoNumero
            data=data.decode()
            data=json.loads(data)
            primoNumero=data['primoNumero']
            operazione=data['operazione']
            secondoNumero=data['secondoNumero']
            #Sequenza di if ed elif per cui scelgo nel "ris" la tipologia di operazione e,
            #infine, eseguo l'operazione stessa, per poi alla fine visualizzare il tutto.
            ris=""
            if operazione=="+":
                ris=primoNumero+secondoNumero
            elif operazione=="-":
                ris=primoNumero-secondoNumero
            elif operazione=="*":
                ris=primoNumero*secondoNumero
            elif operazione=="/":
                #Questo è un controllo per cui indico, ad esempio, che non si può dividere per 0.
                if secondoNumero==0:
                    ris="Non puoi dividere per 0"
                else:
                    ris=primoNumero/secondoNumero
            elif operazione=="%":
                ris=primoNumero%secondoNumero
            else:
                ris="Operazione non riuscita"
            ris=str(ris)#Casting a stringa
            #risposta al client
            sock_service.sendall(ris.encode("UTF-8"))
            #Fine parte server
        sock_service.close()

s1=Server(SERVER_ADDRESS, SERVER_PORT)
sock_list=s1.avvia_server()
s1.accetta_connessioni(sock_list)